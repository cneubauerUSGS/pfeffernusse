from glob import glob
import os

import spiceypy as spice
from pfeffernusse import config


def get_isd(label):

    mission_name = {
        "CASSINI-HUYGENS" : "CASSINI"
    }

    instrument_names = {
        "ISSNA" : "CASSINI_ISS_NAC",
        "ISSWA" : "CASSINI_ISS_WAC"
    }

    metakernal_dir = config.cassini
    mks = sorted(glob(metakernal_dir+'/*.tm'))

    instrument_name = instrument_names[label['INSTRUMENT_ID']]
    spacecraft_name = mission_name[label['MISSION_NAME']]
    target_name = label['TARGET_NAME']
    time = label['START_TIME']

    cassini_mk = None
    for mk in mks:
        if str(time.year) in os.path.basename(mk):
            cassini_mk = mk

    spice.furnsh(cassini_mk)

    # Spice likes ids over names, so grab the ids from the names
    spacecraft_id = spice.bods2c(spacecraft_name)
    instrument_id = spice.bods2c(instrument_name)

    # Load the instrument and target metadata into the ISD
    reference_frame = 'IAU_{}'.format(target_name)

    isd = {}

    rad = spice.bodvrd(target_name, 'RADII', 3)
    isd['semimajor'] = rad[1][0] * 1000
    isd['semiminor'] = rad[1][1] * 1000

    # transx and transy are unavailable so fill in with pixel_size after conversion to millimeters from microns
    # assuming pixels are square
    pixel_size = int(spice.gipool('INS{}_PIXEL_SIZE'.format(instrument_id), 0, 1)[0]) * 0.001
    isd['focal2pixel_samples'] = [0.0, pixel_size, 0.0]
    isd['focal2pixel_lines'] = [0.0, 0.0, pixel_size]

    # unavailable so default to 0
    isd['starting_detector_sample'] = 0.0
    isd['starting_detector_line'] = 0.0

    isd['image_lines'] = float(spice.gipool('INS{}_PIXEL_LINES'.format(instrument_id), 0, 1)[0])
    isd['image_samples'] = float(spice.gipool('INS{}_PIXEL_SAMPLES'.format(instrument_id), 0, 1)[0])

    isd['focal_length_model'] = {}
    isd['focal_length_model']['focal_length'] = float(spice.gdpool('INS{}_FOCAL_LENGTH'.format(instrument_id), 0, 1)[0])
    isd['focal_length_model']['focal_length_epsilon'] = float(spice.gdpool('INS{}_FL_UNCERTAINTY'.format(instrument_id), 0, 1)[0])

    # this following part is ripped from the mdis driver. Since they are both framers this code should be able to be applied to both
    # Now time
    sclock = label['SPACECRAFT_CLOCK_START_COUNT']
    exposure_duration = label['EXPOSURE_DURATION'].value
    exposure_duration = exposure_duration * 0.001  # Scale to seconds

    # Get the instrument id, and, since this is a framer, set the time to the middle of the exposure
    start_et = spice.scs2e(spacecraft_id, sclock)
    start_et += (exposure_duration / 2.0)

    end_et = spice.scs2e(spacecraft_id, label['SPACECRAFT_CLOCK_STOP_COUNT']) + (exposure_duration / 2.0)
    del_et = end_et - start_et
    et = (start_et + end_et)/2

    isd['starting_ephemeris_time'] = start_et
    isd['dt_ephemeris'] = del_et
    isd['number_of_ephemerides'] = 1
    isd['interpolation_method'] = 'lagrange'
    isd['center_ephemeris_time'] = et

    # Get the rotation angles from MDIS NAC frame to Mercury body-fixed frame
    camera2bodyfixed = spice.pxform(instrument_name, reference_frame, et)
    quat = spice.m2q(camera2bodyfixed)
    # cassini follows spice style for quaternions so no transformation is needed
    isd['sensor_orientation'] = list(quat)

    # Get the Sensor Position
    loc, _ = spice.spkpos(target_name, et, reference_frame, 'None', spacecraft_name)
    loc *= -1000

    isd['sensor_location'] = {}
    isd['sensor_location']['x'] = loc[0]
    isd['sensor_location']['y'] = loc[1]
    isd['sensor_location']['z'] = loc[2]
    isd['sensor_location']['unit'] = 'm'


    # Get the velocity
    v_state, lt = spice.spkezr(spacecraft_name,
                                       et,
                                       reference_frame,
                                       'NONE',
                                       target_name)

    isd['sensor_velocity'] = {}
    isd['sensor_velocity']['x'] = v_state[3] * 1000
    isd['sensor_velocity']['y'] = v_state[4] * 1000
    isd['sensor_velocity']['z'] = v_state[5] * 1000
    isd['sensor_velocity']['unit'] = 'm'
    isd['reference_height'] = {}
    isd['reference_height']['minheight'] = label.get('min_valid_height' ,-8000)
    isd['reference_height']['maxheight'] = label.get('max_valid_height', 8000)
    isd['reference_height']['unit'] = 'KM'


    # Get the sun position
    sun_state, lt = spice.spkezr("SUN",
                                 et,
                                 reference_frame,
                                 'NONE',
                                 target_name)

    # lighttime should always be off
    isd['sun_position'] = {}
    isd['sun_position']['x'] = sun_state[0] * 1000
    isd['sun_position']['y'] = sun_state[1] * 1000
    isd['sun_position']['z'] = sun_state[2] * 1000

    isd['sun_velocity'] = {}
    isd['sun_velocity']['x'] = sun_state[3] * 1000
    isd['sun_velocity']['y'] = sun_state[4] * 1000
    isd['sun_velocity']['z'] = sun_state[5] * 1000
    
    # cassini has no optical distortion model
    isd['optical_distortion'] = None

    return isd

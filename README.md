# Swagger generated server

## Overview
This server was generated by the [swagger-codegen](https://github.com/swagger-api/swagger-codegen) project. By using the
[OpenAPI-Spec](https://github.com/swagger-api/swagger-core/wiki) from a remote server, you can easily generate a server stub.  This
is an example of building a swagger-enabled Flask server.

This example uses the [Connexion](https://github.com/zalando/connexion) library on top of Flask.

## Requirements
Python 3.5.2+

## Usage
To run the server, please execute the following from the root directory:

```
pip3 install -r requirements.txt
python3 -m pfeffernusse
```

and open your browser to here:

```
http://localhost:8080/v1/ui/
```

Your Swagger definition lives here:

```
http://localhost:8080/v1/swagger.json
```

To launch the integration tests, use tox:
```
sudo pip install tox
tox
```

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
# building the image
docker build -t pfeffernusse .

# starting up a container
docker run -p 8080:8080 pfeffernusse
```

## Sample Query
First, create a file called mdis_lable.json with the following content.

```json
{
	"label": "PDS_VERSION_ID = PDS3\n\n/*** FILE FORMAT ***/\nRECORD_TYPE = FIXED_LENGTH\nRECORD_BYTES = 1024\nFILE_RECORDS = 1031\nLABEL_RECORDS = 0007\n\n/*** POINTERS TO START BYTE OFFSET OF OBJECTS IN IMAGE FILE ***/\n^IMAGE  = 0008\n\n/*** GENERAL DATA DESCRIPTION PARAMETERS ***/\nMISSION_NAME = \"MESSENGER\"\nINSTRUMENT_HOST_NAME = \"MESSENGER\"\nDATA_SET_ID = \"MESS-E/V/H-MDIS-2-EDR-RAWDATA-V1.0\"\nDATA_QUALITY_ID      = \"0000000000000000\"\nPRODUCT_ID  = \"EN1007907102M\"\nPRODUCT_VERSION_ID   = \"3\"\nSOURCE_PRODUCT_ID    = (\"1007907102_IM5WV\")\nPRODUCER_INSTITUTION_NAME = \"APPLIED COHERENT TECHNOLOGY CORPORATION\"\nSOFTWARE_NAME   = \"MDIS2EDR\"\nSOFTWARE_VERSION_ID  = \"1.1\"\nMISSION_PHASE_NAME   = \"MERCURY ORBIT YEAR 3\"\nTARGET_NAME = \"MERCURY\"\nSEQUENCE_NAME   = \"N/A\"\nOBSERVATION_ID  = \"3855909\"\nOBSERVATION_TYPE     = (\"Monochrome\",\"Targeted\")\nSITE_ID     = \"7211\"\n\n/*** TIME PARAMETERS ***/\nSTART_TIME  = 2013-04-10T08:38:23.299003\nSTOP_TIME   = 2013-04-10T08:38:23.315003\nSPACECRAFT_CLOCK_START_COUNT = \"2/0007907102:974000\"\nSPACECRAFT_CLOCK_STOP_COUNT = \"2/0007907102:990000\"\nORBIT_NUMBER = 1874\nPRODUCT_CREATION_TIME = 2013-04-12T21:00:36\n\n/***  INSTRUMENT ENGINEERING PARAMETERS ***/\nINSTRUMENT_NAME      = \"MERCURY DUAL IMAGING SYSTEM NARROW ANGLE CAMERA\"\nINSTRUMENT_ID   = \"MDIS-NAC\"\nFILTER_NAME = \"748 BP 53\"\nFILTER_NUMBER   = \"N/A\"\nCENTER_FILTER_WAVELENGTH = 747.7 <NM>\nBANDWIDTH   = 52.6 <NM>\nEXPOSURE_DURATION    = 16 <MS>\nEXPOSURE_TYPE   = AUTO\nDETECTOR_TEMPERATURE = -38.99 <DEGC>\nFOCAL_PLANE_TEMPERATURE = -27.22 <DEGC>\nFILTER_TEMPERATURE   = \"N/A\"\nOPTICS_TEMPERATURE   = -26.18 <DEGC>\n\n/*** INSTRUMENT RAW PARAMETERS ***/\nMESS:MET_EXP = 7907102\nMESS:IMG_ID_LSB      = 54821\nMESS:IMG_ID_MSB      = 58\nMESS:ATT_CLOCK_COUNT = 7907100\nMESS:ATT_Q1 = 0.90576386\nMESS:ATT_Q2 = -0.05492725\nMESS:ATT_Q3 = 0.38405561\nMESS:ATT_Q4 = -0.17051725\nMESS:ATT_FLAG   = 7\nMESS:PIV_POS_MOTOR   = 24374\nMESS:PIV_GOAL   = \"N/A\"\nMESS:PIV_POS = -514\nMESS:PIV_READ   = 24804\nMESS:PIV_CAL = -26758\nMESS:FW_GOAL = 11976\nMESS:FW_POS = 11864\nMESS:FW_READ = 11864\nMESS:CCD_TEMP   = 1039\nMESS:CAM_T1 = 471\nMESS:CAM_T2 = 501\nMESS:EXPOSURE   = 16\nMESS:DPU_ID = 0\nMESS:IMAGER = 1\nMESS:SOURCE = 0\nMESS:FPU_BIN = 0\nMESS:COMP12_8   = 1\nMESS:COMP_ALG   = 1\nMESS:COMP_FST   = 1\nMESS:TIME_PLS   = 2\nMESS:LATCH_UP   = 0\nMESS:EXP_MODE   = 1\nMESS:PIV_STAT   = 3\nMESS:PIV_MPEN   = 0\nMESS:PIV_PV = 1\nMESS:PIV_RV = 1\nMESS:FW_PV  = 1\nMESS:FW_RV  = 1\nMESS:AEX_STAT   = 768\nMESS:AEX_STHR   = 5\nMESS:AEX_TGTB   = 1830\nMESS:AEX_BACB   = 240\nMESS:AEX_MAXE   = 989\nMESS:AEX_MINE   = 1\nMESS:DLNKPRIO   = 5\nMESS:WVLRATIO   = 4\nMESS:PIXELBIN   = 0\nMESS:SUBFRAME   = 0\nMESS:SUBF_X1 = 0\nMESS:SUBF_Y1 = 0\nMESS:SUBF_DX1   = 0\nMESS:SUBF_DY1   = 0\nMESS:SUBF_X2 = 0\nMESS:SUBF_Y2 = 0\nMESS:SUBF_DX2   = 0\nMESS:SUBF_DY2   = 0\nMESS:SUBF_X3 = 0\nMESS:SUBF_Y3 = 0\nMESS:SUBF_DX3   = 0\nMESS:SUBF_DY3   = 0\nMESS:SUBF_X4 = 0\nMESS:SUBF_Y4 = 0\nMESS:SUBF_DX4   = 0\nMESS:SUBF_DY4   = 0\nMESS:SUBF_X5 = 0\nMESS:SUBF_Y5 = 0\nMESS:SUBF_DX5   = 0\nMESS:SUBF_DY5   = 0\nMESS:CRITOPNV   = 0\nMESS:JAILBARS   = 0\nMESS:JB_X0  = 0\nMESS:JB_X1  = 0\nMESS:JB_SPACE   = 0\n\n/*** GEOMETRY INFORMATION ***/\nRIGHT_ASCENSION      = 23.68923 <DEG>\nDECLINATION = -38.62166 <DEG>\nTWIST_ANGLE = 210.03318 <DEG>\nRA_DEC_REF_PIXEL     = (512.00000,512.00000)\nRETICLE_POINT_RA     = (24.02532 <DEG>,22.38962 <DEG>,24.99625 <DEG>,23.32781\n  <DEG>)\nRETICLE_POINT_DECLINATION = (-37.59907 <DEG>,-38.33408 <DEG>,-38.88264 <DEG>,\n  -39.63687 <DEG>)\n\n/*** TARGET PARAMETERS ***/\nSC_TARGET_POSITION_VECTOR = (-2445.36922 <KM>,-575.95803 <KM>,2318.04382 <KM>)\nTARGET_CENTER_DISTANCE = 3418.31617 <KM>\n\n/*** TARGET WITHIN SENSOR FOV ***/\nSLANT_DISTANCE  = 995.14184 <KM>\nCENTER_LATITUDE      = 36.62113 <DEG>\nCENTER_LONGITUDE     = 305.30485 <DEG>\nHORIZONTAL_PIXEL_SCALE = 25.37158 <M>\nVERTICAL_PIXEL_SCALE = 25.37158 <M>\nSMEAR_MAGNITUDE      = 1.33377 <PIXELS>\nSMEAR_AZIMUTH   = 284.79052 <DEG>\nNORTH_AZIMUTH   = 286.23036 <DEG>\nRETICLE_POINT_LATITUDE = (36.82656 <DEG>,37.00217 <DEG>,36.24112 <DEG>,\n  36.42013 <DEG>)\nRETICLE_POINT_LONGITUDE = (304.82264 <DEG>,305.56665 <DEG>,305.03944 <DEG>,\n  305.78280 <DEG>)\n\n/*** SPACECRAFT POSITION WITH RESPECT TO CENTRAL BODY ***/\nSUB_SPACECRAFT_LATITUDE = 37.53549 <DEG>\nSUB_SPACECRAFT_LONGITUDE = 309.69009 <DEG>\nSPACECRAFT_ALTITUDE  = 978.31617 <KM>\nSUB_SPACECRAFT_AZIMUTH = 0.59551 <DEG>\n\n/*** SPACECRAFT LOCATION ***/\nSPACECRAFT_SOLAR_DISTANCE = 68395689.43432 <KM>\nSC_SUN_POSITION_VECTOR = (12256870.78372 <KM>,-58815922.56555 <KM>,\n  -32686797.09838 <KM>)\nSC_SUN_VELOCITY_VECTOR = (-35.02846 <KM/S>,-12.10883 <KM/S>,-1.29292 <KM/S>)\n\n/*** VIEWING AND LIGHTING GEOMETRY (SUN ON TARGET) ***/\nSOLAR_DISTANCE  = 68396740.25771 <KM>\nSUB_SOLAR_AZIMUTH    = 179.44333 <DEG>\nSUB_SOLAR_LATITUDE   = -0.03364 <DEG>\nSUB_SOLAR_LONGITUDE  = 242.52925 <DEG>\nINCIDENCE_ANGLE      = 68.48232 <DEG>\nPHASE_ANGLE = 80.99098 <DEG>\nEMISSION_ANGLE  = 12.51093 <DEG>\nLOCAL_HOUR_ANGLE     = 242.77561 <DEG>\n\n/*** GEOMETRY FOR EACH SUBFRAME ***/\nGROUP = SUBFRAME1_PARAMETERS\n  RETICLE_POINT_LATITUDE = (\"N/A\",\"N/A\",\"N/A\",\"N/A\")\n  RETICLE_POINT_LONGITUDE = (\"N/A\",\"N/A\",\"N/A\",\"N/A\")\nEND_GROUP = SUBFRAME1_PARAMETERS\n\nGROUP = SUBFRAME2_PARAMETERS\n  RETICLE_POINT_LATITUDE = (\"N/A\",\"N/A\",\"N/A\",\"N/A\")\n  RETICLE_POINT_LONGITUDE = (\"N/A\",\"N/A\",\"N/A\",\"N/A\")\nEND_GROUP = SUBFRAME2_PARAMETERS\n\nGROUP = SUBFRAME3_PARAMETERS\n  RETICLE_POINT_LATITUDE = (\"N/A\",\"N/A\",\"N/A\",\"N/A\")\n  RETICLE_POINT_LONGITUDE = (\"N/A\",\"N/A\",\"N/A\",\"N/A\")\nEND_GROUP = SUBFRAME3_PARAMETERS\n\nGROUP = SUBFRAME4_PARAMETERS\n  RETICLE_POINT_LATITUDE = (\"N/A\",\"N/A\",\"N/A\",\"N/A\")\n  RETICLE_POINT_LONGITUDE = (\"N/A\",\"N/A\",\"N/A\",\"N/A\")\nEND_GROUP = SUBFRAME4_PARAMETERS\n\nGROUP = SUBFRAME5_PARAMETERS\n  RETICLE_POINT_LATITUDE = (\"N/A\",\"N/A\",\"N/A\",\"N/A\")\n  RETICLE_POINT_LONGITUDE = (\"N/A\",\"N/A\",\"N/A\",\"N/A\")\nEND_GROUP = SUBFRAME5_PARAMETERS\n\n\nOBJECT = IMAGE\n  LINES     = 1024\n  LINE_SAMPLES  = 1024\n  SAMPLE_TYPE   = UNSIGNED_INTEGER\n  SAMPLE_BITS   = 8\n  UNIT      = \"N/A\"\n  DARK_STRIP_MEAN    = 33.204\n\n/*** IMAGE STATISTICS OF  ***/\n/*** THE EXPOSED CCD AREA ***/\n  MINIMUM   = 37.000\n  MAXIMUM   = 111.000\n  MEAN      = 73.735\n  STANDARD_DEVIATION = 6.234\n\n/*** PIXEL COUNTS ***/\n  SATURATED_PIXEL_COUNT = 0\n  MISSING_PIXELS     = 0\nEND_OBJECT = IMAGE\nEND"
}
```

Once created, execute the following:
`curl -X POST "http://pfeffer.wr.usgs.gov/v1/pds/" -H  "accept: application/json" -H  "Content-Type: application/json" -d @mdis_label.json`

The result should be a CSM compliant ISD file, e.g.:

```json
{
  "center_ephemeris_time": 418855170.5006496,
  "dt_ephemeris": 0.016000032424926758,
  "focal2pixel_lines": [
    0.0,
    0.0,
    0.014
  ],
  "focal2pixel_samples": [
    0.0,
    0.014,
    0.0
  ],
  "focal_length_model": {
    "focal_length": 549.1178195372703,
    "focal_length_epsilon": 0.5
  },
  "image_lines": 1024,
  "image_samples": 1024,
  "interpolation_method": "lagrange",
  "number_of_ephemerides": 1,
  "optical_distortion": {
    "coefficients": [
      0.0,
      0.0,
      1.0,
      0.0009060010594996751,
      0.0,
      0.0003574842626620758,
      0.0,
      1.004010471468856e-05,
      0.0,
      1.004010471468856e-05
    ]
  },
  "reference_height": {
    "maxheight": 8000,
    "minheight": -8000,
    "unit": "KM"
  },
  "semimajor": 2439400.0,
  "semiminor": 2439400.0,
  "sensor_location": {
    "unit": "m",
    "x": 1728197.0439980691,
    "y": -2088216.968709019,
    "z": 2082694.211007305
  },
  "sensor_orientation": [
    0.39900625946972035,
    -0.7905943518879116,
    -0.4359092364938529,
    0.1604297765574143
  ],
  "sensor_velocity": {
    "unit": "m",
    "x": 1997.972055920044,
    "y": -1800.5700851538286,
    "z": -1674.779510619489
  },
  "starting_detector_line": 1,
  "starting_detector_sample": 9,
  "starting_ephemeris_time": 418855170.49264956,
  "sun_position": {
    "x": -31640702432.921574,
    "y": -60638093688.3111,
    "z": -38731104.56773266
  },
  "sun_velocity": {
    "x": -38191.12392266652,
    "y": 24381.841914284098,
    "z": -4.860970418599342
  }
}
```

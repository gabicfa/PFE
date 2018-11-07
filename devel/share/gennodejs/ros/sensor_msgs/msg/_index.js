
"use strict";

let PointCloud2 = require('./PointCloud2.js');
let FluidPressure = require('./FluidPressure.js');
let BatteryState = require('./BatteryState.js');
let CompressedImage = require('./CompressedImage.js');
let JointState = require('./JointState.js');
let Joy = require('./Joy.js');
let LaserScan = require('./LaserScan.js');
let MultiEchoLaserScan = require('./MultiEchoLaserScan.js');
let Image = require('./Image.js');
let NavSatStatus = require('./NavSatStatus.js');
let NavSatFix = require('./NavSatFix.js');
let PointCloud = require('./PointCloud.js');
let MultiDOFJointState = require('./MultiDOFJointState.js');
let LaserEcho = require('./LaserEcho.js');
let MagneticField = require('./MagneticField.js');
let CameraInfo = require('./CameraInfo.js');
let TimeReference = require('./TimeReference.js');
let PointField = require('./PointField.js');
let Range = require('./Range.js');
let Illuminance = require('./Illuminance.js');
let Temperature = require('./Temperature.js');
let JoyFeedbackArray = require('./JoyFeedbackArray.js');
let JoyFeedback = require('./JoyFeedback.js');
let Imu = require('./Imu.js');
let ChannelFloat32 = require('./ChannelFloat32.js');
let RegionOfInterest = require('./RegionOfInterest.js');
let RelativeHumidity = require('./RelativeHumidity.js');

module.exports = {
  PointCloud2: PointCloud2,
  FluidPressure: FluidPressure,
  BatteryState: BatteryState,
  CompressedImage: CompressedImage,
  JointState: JointState,
  Joy: Joy,
  LaserScan: LaserScan,
  MultiEchoLaserScan: MultiEchoLaserScan,
  Image: Image,
  NavSatStatus: NavSatStatus,
  NavSatFix: NavSatFix,
  PointCloud: PointCloud,
  MultiDOFJointState: MultiDOFJointState,
  LaserEcho: LaserEcho,
  MagneticField: MagneticField,
  CameraInfo: CameraInfo,
  TimeReference: TimeReference,
  PointField: PointField,
  Range: Range,
  Illuminance: Illuminance,
  Temperature: Temperature,
  JoyFeedbackArray: JoyFeedbackArray,
  JoyFeedback: JoyFeedback,
  Imu: Imu,
  ChannelFloat32: ChannelFloat32,
  RegionOfInterest: RegionOfInterest,
  RelativeHumidity: RelativeHumidity,
};

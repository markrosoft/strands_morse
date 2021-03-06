from morse.builder import *


class Scitosa5(Robot):
    WITH_CAMERAS = 1
    WITHOUT_DEPTHCAMS = 2
    WITHOUT_CAMERAS = 3

    """
    A template robot model for scitosA5
    """
    def __init__(self, with_cameras = 1):

        # scitosA5.blend is located in the data/robots directory
        Robot.__init__(self, 'strands_sim/robots/scitosA5.blend')

        self.properties(classpath = "strands_sim.robots.scitosA5.Scitosa5")

        # The list of the main methods to manipulate your components
        # is here: http://www.openrobots.org/morse/doc/stable/user/builder_overview.html
        self.add_interface('ros')

        ###################################
        # Actuators
        ###################################

        # Motion control
        self.motion = MotionVW()
        self.append(self.motion)
        self.motion.add_interface('ros', topic='/cmd_vel')

        # Keyboard control
        self.keyboard = Keyboard()
        self.append(self.keyboard)

        self.ptu = PTU() # creates a new instance of the actuator
        self.append(self.ptu)
        self.ptu.translate(0, 0, 1.585)
        self.ptu.rotate(0, 0, 0)
        self.ptu.add_interface('ros', topic='/ptu')

        ###################################
        # Sensors
        ###################################
        
        # Battery
        self.battery = Battery()
        self.battery.translate(x=0.0,z=0.0)
        self.append(self.battery)
        self.battery.add_interface('ros', topic="/battery")

        # Odometry
        self.odometry = Odometry()
        self.append(self.odometry)
        self.odometry.add_interface('ros', topic="/odom")

        # Laserscanner
        self.scan = Hokuyo()
        self.scan.translate(x=0.30, z=0.386)
        self.append(self.scan)
        self.scan.properties(Visible_arc = False)
        self.scan.properties(laser_range = 30.0)
        self.scan.properties(resolution = 1.0)
        self.scan.properties(scan_window = 180.0)
        self.scan.create_laser_arc()
        self.scan.add_interface('ros', topic='/scan')

        if with_cameras < Scitosa5.WITHOUT_CAMERAS:
            self.videocam = VideoCamera()
            self.ptu.append(self.videocam)
            self.videocam.translate(0.04, -0.04, 0.065)
            self.videocam.rotate(0, 0, 0)
            self.videocam.add_interface('ros', topic='/videocam')
            
            # Semantic Camera
            self.semanticcamera = SemanticCamera()
            self.ptu.append(self.semanticcamera)
            self.semanticcamera.translate(0.04, 0.04, 0.065)
            self.semanticcamera.rotate(0.0, 0.0, 0.0)
            self.semanticcamera.add_interface('ros', topic='/semcam')
            
            if with_cameras < Scitosa5.WITHOUT_DEPTHCAMS:
                # Depth camera
                self.depthcam = DepthCamera() # Kinect() RVIZ crashes when depthcam data is visualized!?
                self.ptu.append(self.depthcam)
                self.depthcam.translate(0.04, -0.04, 0.065)
                self.depthcam.rotate(0, 0, 0)
                self.depthcam.add_interface('ros', topic='/depthcam')





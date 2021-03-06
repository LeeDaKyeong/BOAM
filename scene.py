import os
import scenedetect.manager
import scenedetect.detectors

def detection(path = None, filename = None):
    print("[PySceneDetect] Starts", filename, "SceneDetection")

    # Set mode of detector
    content_detector = scenedetect.detectors.ContentDetector(threshold = 40)

    # Set SceneManager
    smgr = scenedetect.manager.SceneManager(detector = content_detector, frame_skip = 3)

    # Scene detection
    scenedetect.detect_scenes_file(path + filename, smgr)

    return smgr.scene_list
from maya import cmds

flipCamGrpExists = cmds.objExists('flipCamGrp')
if flipCamGrpExists:
    scaleXvalue = cmds.getAttr('flipCamGrp.scaleX')
    if scaleXvalue == -1:
        cmds.setAttr('flipCamGrp.scaleX', 1, e=True)
        print 'Now normal camera'
    elif scaleXvalue == 1:
        cmds.setAttr('flipCamGrp.scaleX', -1, e=True)
        print 'Now mirrored camera'
    else:
        print 'Looks like your Scale X Attr is wonky.  Needs to be 1 or -1.'
else:
    shotCam = cmds.ls(selection=True)[0]
    flipCam = cmds.camera(name='flipCam1')[0]
    flipCamGrp = cmds.group(flipCam, name='flipCamGrp')
    cmds.parentConstraint(shotCam, flipCamGrp, mo=False)
    cmds.setAttr(str('{}Shape.{}'.format(flipCam, 'displayFilmGate')), e=True, av=1)
    camShapeAttrs = ['focalLength', 'cameraScale', 'horizontalFilmAperture', 'verticalFilmAperture', 'lensSqueezeRatio',
                     'filmFitOffset', 'horizontalFilmOffset', 'verticalFilmOffset', 'preScale', 'filmTranslateH',
                     'filmTranslateV', 'postScale', 'fStop', 'overscan', 'focusDistance', 'shutterAngle',
                     'nearClipPlane', 'farClipPlane']
    for attr in camShapeAttrs:
        shotCamAttr = str('{}Shape.{}'.format(shotCam, attr))
        flipCamAttr = str('{}Shape1.{}'.format(flipCam, attr))
        cmds.connectAttr(shotCamAttr, flipCamAttr, f=True)

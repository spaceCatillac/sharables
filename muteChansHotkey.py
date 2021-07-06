# This python is for animators to quickly mute and unmute channels they pre select for Autodesk Maya.  
# Setup Step1: Copy and paste the first section, down to the line of hashtags, to a python tab in Maya. 
# Setup Step2: Then middle click drag that section to a custom shelf.
# Setup Step3: Copy and paste the 2nd section, below the line of hashtags, to your preferred hotkey or...
# Setup Step4: ...repeat step2 if you want a shelf button. (You can do both)

# How to use Step1: Select the objects and then the channels you want to mute/unmute in the channel box.
# How to use Step2: Click your first shelf button to save those channels
# How to use Step3: Now use your hotkey or 2nd shelf button to quickly mute/unmute those channels

from maya import cmds
def getSelectedChannels():
    if not cmds.ls(sl=True):
        return
    gChannelBoxName = mel.eval('$temp=$gChannelBoxName')
    sma = cmds.channelBox(gChannelBoxName, query=True, sma=True)
    ssa = cmds.channelBox(gChannelBoxName, query=True, ssa=True)
    sha = cmds.channelBox(gChannelBoxName, query=True, sha=True)
    channels = list()
    if sma:
        channels.extend(sma)
    if ssa:
        channels.extend(ssa)
    if sha:
        channels.extend(sha)
    return channels 
chans = getSelectedChannels()

attrsToMute = []
objs = cmds.ls(sl=True)
for obj in objs:
    for chan in chans:
        attr = '{}.{}'.format(obj, chan)
        attrsToMute.append(attr)

#########################################################

if 'attrsToMute' in locals():
    muteState = cmds.mute(attrsToMute[0], q=True)
    if not muteState:
        cmds.mute(attrsToMute, force=True)
    else:
        cmds.mute(attrsToMute, disable=True, force=True)
else:
    objs = cmds.ls(sl=True)
    muteState = cmds.mute('{}.tx'.format(objs[0]), q=True)
    if not muteState:
        cmds.mute(objs, force=True)
    else:
        cmds.mute(objs, disable=True, force=True)

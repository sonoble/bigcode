#!/usr/bin/python3
"""VPI (Virtual Port Interface) wrapper module.

Copyright 2013, Big Switch Networks, Inc.

Licensed under the Eclipse Public License, Version 1.0 (the
"License"); you may not use this file except in compliance
with the License. You may obtain a copy of the License at

    http://www.eclipse.org/legal/epl-v10.html

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific
language governing permissions and limitations under the
License.

Wrapper object class for use with the pyvpi library.
"""

import sys

# Hack. For the pyvpi.so library from the libvpi package.
sys.path.append("/usr/lib")
import pyvpi


class Vpi:
    """Wrapper class for the pyvpi library."""

    def __init__(self, create_spec):
        self.v = pyvpi.Create(create_spec)

    def NameGet(self):
        return pyvpi.NameGet(self.v)

    def NameSet(self, new_name):
        return pyvpi.NameSet(self.v, new_name)

    def GetCreateSpec(self):
        return pyvpi.GetCreateSpec(self.v)

    def DescriptorGet(self):
        return pyvpi.DescriptorGet(self.v)

    def Ref(self):
        return pyvpi.Ref(self.v)

    def Unref(self):
        return pyvpi.Unref(self.v)

    def GetRecvSpec(self):
        return pyvpi.GetRecvSpec(self.v)

    def GetSendToSpec(self):
        return pyvpi.GetSendToSpec(self.v)

    def AddRecvListener(self, listener):
        if isinstance(listener, str):
            return pyvpi.AddRecvListenerSpec(self.v, listener)
        else:
            return pyvpi.AddRecvListener(self.v, listener)

    def RemoveRecvListener(self, listener):
        if isinstance(listener, str):
            return pyvpi.RemoveRecvListenerSpec(self.v, listener)
        else:
            return pyvpi.RemoveRecvListener(self.v, listener)

    def RecvListenerCount(self):
        return pyvpi.RecvListenerCount(self.v)

    def RecvListenersDrop(self):
        return pyvpi.RecvListenersDrop(self.v)

    def AddSendListener(self, listener):
        if isinstance(listener, str):
            return pyvpi.AddSendListenerSpec(self.v, listener)
        else:
            return pyvpi.AddSendListener(self.v, listener)

    def RemoveSendListener(self, listener):
        if isinstance(listener, str):
            return pyvpi.RemoveSendListenerSpec(self.v, listener)
        else:
            return pyvpi.RemoveSendListener(self.v, listener)

    def SendListenerCount(self):
        return pyvpi.SendListenerCount(self.v)

    def SendListenersDrop(self):
        return pyvpi.SendListenersDrop(self.v)

    def AddSendRecvListener(self, listener):
        if isinstance(listener, str):
            return pyvpi.AddSendRecvListenerSpec(self.v, listener)
        else:
            return pyvpi.AddSendRecvListener(self.v, listener)

    def RemoveSendRecvListener(self, listener):
        if isinstance(listener, str):
            return pyvpi.RemoveSendRecvListenerSpec(self.v, listener)
        else:
            return pyvpi.RemoveSendRecvListener(self.v, listener)

    def SendRecvListenerCount(self):
        return pyvpi.SendRecvListenerCount(self.v)

    def SendRecvListenersDrop(self):
        return pyvpi.SendRecvListenersDrop(self.v)

    def TypeGet(self):
        return pyvpi.TypeGet(self.v)

    def Send(self, data):
        return pyvpi.Send(self.v, data)

    def Ioctl(self, cmd, data):
        return pyvpi.Ioctl(self.v, cmd, data)

    def Recv(self, block):
        return pyvpi.Recv(self.v, block)

    def Drain(self):
        return pyvpi.Drain(self.v)

    def ConfigShow(self):
        return pyvpi.ConfigShow(self.v)


class VpiBridge:
    """Bridge between two VPI interfaces."""

    def __init__(self, v1_in, v2_in):
        # v1 and or v2 can be Vpi objects or create specs.
        if isinstance(v1_in, Vpi):
            self.v1 = v1_in
        else:
            self.v1 = Vpi(v1_in)

        if isinstance(v2_in, Vpi):
            self.v2 = v2_in
        else:
            self.v2 = Vpi(v2_in)

        print(self.v1.NameGet())
        print(self.v2.NameGet())

        self.bridge = pyvpi.BridgeCreate(self.v1.v, self.v2.v)

    def Start(self):
        return pyvpi.BridgeStart(self.bridge)

    def Stop(self):
        return pyvpi.BridgeStop(self.bridge)


class VpiTool:
    """Utility class for VPI operations."""

    def __init__(self):
        pass

    def Bridge(self, v1, v2):
        rv = VpiBridge(v1, v2)
        rv.Start()
        return rv

    def Dump(self, v1):
        v = Vpi(v1)
        count = 0
        while True:
            data = v.Recv(True)
            print("[%.3d]" % count)
            print(data)
            count = count + 1

    def Send(self, v1, data):
        v = Vpi(v1)
        v.Send(data)

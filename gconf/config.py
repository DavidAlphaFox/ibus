# vim:set et sts=4 sw=4:
#
# ibus - The Input Bus
#
# Copyright(c) 2007-2008 Huang Peng <shawn.p.huang@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or(at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330,
# Boston, MA  02111-1307  USA

__all__ = (
    "Config",
)

import gobject
try:
    import gconf
except:
    from ibus import gconf
import dbus
import ibus

GCONF_IBUS_PATH = "/desktop/ibus"

class Config(ibus.ConfigBase):
    __gsignals__ = {
        "value-changed" : (
            gobject.SIGNAL_RUN_FIRST,
            gobject.TYPE_NONE,
            (gobject.TYPE_STRING, gobject.TYPE_STRING, gobject.TYPE_PYOBJECT)),
    }

    def __init__ (self, bus):
        super(Config, self).__init__(bus)
        self.__client = gconf.Client()
        self.__handler_id = self.__client.connect("value-changed", self.__value_changed_cb)
        self.__client.add_dir(GCONF_IBUS_PATH, gconf.CLIENT_PRELOAD_NONE)

    def get_value(self, section, name):
        key = "/".join([GCONF_IBUS_PATH, section, name])
        value = self.__client.get(key)
        if value == None:
            raise ibus.IBusException("key = \"%s\" does not exist" % key)
        return self.__to_py_value(value)

    def set_value(self, section, name, value):
        key = "/".join([GCONF_IBUS_PATH, section, name])
        value = self.__to_gconf_value(value)
        self.__client.set(key, value)

    def do_destroy(self):
        if self.__client:
            self.__client.disconnect(self.__handler_id)
            self.__client = None
        super(Config, self).do_destroy()

    def __to_py_value(self, value):
        if value == None:
            return None
        if value.type == gconf.VALUE_STRING:
            return unicode(value.get_string(), "utf-8")
        if value.type == gconf.VALUE_INT:
            return value.get_int()
        if value.type == gconf.VALUE_FLOAT:
            return value.get_float()
        if value.type == gconf.VALUE_BOOL:
            return value.get_bool()
        if value.type == gconf.VALUE_PAIR:
            return (self.__to_py_value(value.get_car()), self.__to_py_value(value.get_cdr()))
        if value.type == gconf.VALUE_LIST:
            return map(self.__to_py_value, value.get_list())
        raise ibus.IBusException("Do not support type == %s" % str(value.type))

    def __to_gconf_value(self, value):
        if isinstance(value, str):
            ret = gconf.Value(gconf.VALUE_STRING)
            ret.set_string(value)
        elif isinstance(value, unicode):
            ret = gconf.Value(gconf.VALUE_STRING)
            ret.set_string(value.encode("utf-8"))
        elif isinstance(value, bool):
            ret = gconf.Value(gconf.VALUE_BOOL)
            ret.set_bool(value)
        elif isinstance(value, int):
            ret = gconf.Value(gconf.VALUE_INT)
            ret.set_int(value)
        elif isinstance(value, float):
            ret = gconf.Value(gconf.VALUE_FLOAT)
            ret.set_float(value)
        elif isinstance(value, tuple):
            if len(value) != 2:
                raise ibus.IBusException("Pair must have two value")
            ret = gconf.Value(gconf.VALUE_PAIR)
            ret.set_car(self.__to_gconf_value(value[0]))
            ret.set_cdr(self.__to_gconf_value(value[1]))
        elif isinstance(value, list):
            ret = gconf.Value(gconf.VALUE_LIST)
            if len(value) > 0:
                value = map(self.__to_gconf_value, value)
                _type = value[0].type
                if any(map(lambda x: x.type != _type, value)):
                    raise ibus.IBusException("Items of a list must be in same type")
                ret.set_list_type(_type)
                ret.set_list(value)
            elif len(value) == 0 and isinstance(value, dbus.Array):
                if value.signature == "i":
                    ret.set_list_type(gconf.VALUE_INT)
                elif value.signature == "s":
                    ret.set_list_type(gconf.VALUE_STRING)
                elif value.signature == "d":
                    ret.set_list_type(gconf.VALUE_FLOAT)
                elif value.signature == "b":
                    ret.set_list_type(gconf.VALUE_BOOL)
                else:
                    pass
        else:
            raise ibus.IBusException("Do not support type of %s." % type(value))
        return ret

    def __value_changed_cb(self, gconf, key, value):
        value = self.__client.get(key)
        value = self.__to_py_value(value)
        if value == None:
            value = 0
        section_name = key.replace(GCONF_IBUS_PATH + "/", "")
        section_name = section_name.rsplit("/", 1)
        if len(section_name) == 1:
            self.value_changed("", section_name[0], value)
        elif len(section_name) == 2:
            self.value_changed(section_name[0], section_name[1], value)
        else:
            print "Can not process %s" % key

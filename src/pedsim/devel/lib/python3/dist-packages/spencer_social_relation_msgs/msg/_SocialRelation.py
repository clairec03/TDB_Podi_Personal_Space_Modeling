# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from spencer_social_relation_msgs/SocialRelation.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SocialRelation(genpy.Message):
  _md5sum = "004e9c919342c749d66dbc051dba51f6"
  _type = "spencer_social_relation_msgs/SocialRelation"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string      type        # e.g. mother-son relationship, romantic relationship, etc.
float32     strength    # relationship strength between 0.0 and 1.0

uint32      track1_id
uint32      track2_id


# Constants for type (just examples at the moment)
string      TYPE_SPATIAL  = "spatial"
string      TYPE_ROMANTIC = "romantic"
string      TYPE_PARENT_CHILD = "parent_child"
string      TYPE_FRIENDSHIP = "friendship\""""
  # Pseudo-constants
  TYPE_SPATIAL = r'"spatial"'
  TYPE_ROMANTIC = r'"romantic"'
  TYPE_PARENT_CHILD = r'"parent_child"'
  TYPE_FRIENDSHIP = r'"friendship"'

  __slots__ = ['type','strength','track1_id','track2_id']
  _slot_types = ['string','float32','uint32','uint32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       type,strength,track1_id,track2_id

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SocialRelation, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.type is None:
        self.type = ''
      if self.strength is None:
        self.strength = 0.
      if self.track1_id is None:
        self.track1_id = 0
      if self.track2_id is None:
        self.track2_id = 0
    else:
      self.type = ''
      self.strength = 0.
      self.track1_id = 0
      self.track2_id = 0

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_f2I().pack(_x.strength, _x.track1_id, _x.track2_id))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.type = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.strength, _x.track1_id, _x.track2_id,) = _get_struct_f2I().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.type
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_f2I().pack(_x.strength, _x.track1_id, _x.track2_id))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.type = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.type = str[start:end]
      _x = self
      start = end
      end += 12
      (_x.strength, _x.track1_id, _x.track2_id,) = _get_struct_f2I().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_f2I = None
def _get_struct_f2I():
    global _struct_f2I
    if _struct_f2I is None:
        _struct_f2I = struct.Struct("<f2I")
    return _struct_f2I

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hello-world.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11hello-world.proto\x12\nhelloworld\"\x0e\n\x0cHelloRequest\"\x1d\n\nHelloReply\x12\x0f\n\x07message\x18\x01 \x01(\t2\x8c\x01\n\x07Greeter\x12>\n\x08SayHello\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x12\x41\n\x0bGetPreHello\x12\x18.helloworld.HelloRequest\x1a\x16.helloworld.HelloReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'hello_world_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_HELLOREQUEST']._serialized_start=33
  _globals['_HELLOREQUEST']._serialized_end=47
  _globals['_HELLOREPLY']._serialized_start=49
  _globals['_HELLOREPLY']._serialized_end=78
  _globals['_GREETER']._serialized_start=81
  _globals['_GREETER']._serialized_end=221
# @@protoc_insertion_point(module_scope)
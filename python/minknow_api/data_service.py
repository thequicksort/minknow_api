### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
from .data_pb2_grpc import *
from . import data_pb2
from minknow_api.data_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging

__all__ = [
    "DataService",
    "GetChannelStatesRequest",
    "GetChannelStatesResponse",
    "GetDataTypesRequest",
    "GetDataTypesResponse",
    "GetSignalBytesRequest",
    "GetSignalBytesResponse",
    "GetSignalMinMaxRequest",
    "GetSignalMinMaxResponse",
    "GetLiveReadsRequest",
    "GetLiveReadsResponse",
    "ResetChannelStatesRequest",
    "ResetChannelStatesResponse",
    "GetReadStatisticsRequest",
    "GetReadStatisticsResponse",
    "LockChannelStatesRequest",
    "LockChannelStatesResponse",
    "UnlockChannelStatesRequest",
    "UnlockChannelStatesResponse",
    "GetExperimentYieldInfoRequest",
    "GetExperimentYieldInfoResponse",
]

def run_with_retry(method, message, timeout, unwraps, full_name):
    retry_count = 20
    error = None
    for i in range(retry_count):
        try:
            result = MessageWrapper(method(message, timeout=timeout), unwraps=unwraps)
            return result
        except grpc.RpcError as e:
            # Retrying unidentified grpc errors to keep clients from crashing
            retryable_error = (e.code() == grpc.StatusCode.UNKNOWN and "Stream removed" in e.details() or \
                                (e.code() == grpc.StatusCode.INTERNAL and "RST_STREAM" in e.details()))
            if retryable_error:
                logging.info('Bypassed ({}: {}) error for grpc: {}. Attempt {}.'.format(e.code(), e.details(), full_name, i))
            else:
                raise
            error = e
        time.sleep(1)
    raise error


class DataService(object):
    def __init__(self, channel):
        self._stub = DataServiceStub(channel)
        self._pb = data_pb2

    def get_channel_states(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_channel_states, _message, _timeout, [], "minknow_api.data.DataService")

        unused_args = set(kwargs.keys())

        _message = GetChannelStatesRequest()

        if "first_channel" in kwargs:
            unused_args.remove("first_channel")
            _message.first_channel = kwargs['first_channel']
        else:
            raise ArgumentError("get_channel_states requires a 'first_channel' argument")

        if "last_channel" in kwargs:
            unused_args.remove("last_channel")
            _message.last_channel = kwargs['last_channel']
        else:
            raise ArgumentError("get_channel_states requires a 'last_channel' argument")

        if "use_channel_states_ids" in kwargs:
            unused_args.remove("use_channel_states_ids")
            _message.use_channel_states_ids.value = kwargs['use_channel_states_ids']

        if "wait_for_processing" in kwargs:
            unused_args.remove("wait_for_processing")
            _message.wait_for_processing = kwargs['wait_for_processing']

        if "heartbeat" in kwargs:
            unused_args.remove("heartbeat")
            _message.heartbeat.CopyFrom(kwargs['heartbeat'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_channel_states: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_channel_states, _message, _timeout, [], "minknow_api.data.DataService")

    def get_data_types(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_data_types, _message, _timeout, [], "minknow_api.data.DataService")

        unused_args = set(kwargs.keys())

        _message = GetDataTypesRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_data_types: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_data_types, _message, _timeout, [], "minknow_api.data.DataService")

    def get_signal_bytes(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_signal_bytes, _message, _timeout, [], "minknow_api.data.DataService")

        unused_args = set(kwargs.keys())

        # check oneof group 'length'
        oneof_fields = set([
            "seconds",
            "samples",
        ])

        if len(unused_args & oneof_fields) > 1:
            raise ArgumentError("get_signal_bytes given multiple conflicting arguments: '{}'".format(", ".join(unused_args & oneof_fields)))

        _message = GetSignalBytesRequest()

        if "seconds" in kwargs:
            unused_args.remove("seconds")
            _message.seconds = kwargs['seconds']

        if "samples" in kwargs:
            unused_args.remove("samples")
            _message.samples = kwargs['samples']

        if "first_channel" in kwargs:
            unused_args.remove("first_channel")
            _message.first_channel = kwargs['first_channel']
        else:
            raise ArgumentError("get_signal_bytes requires a 'first_channel' argument")

        if "last_channel" in kwargs:
            unused_args.remove("last_channel")
            _message.last_channel = kwargs['last_channel']
        else:
            raise ArgumentError("get_signal_bytes requires a 'last_channel' argument")

        if "include_channel_configs" in kwargs:
            unused_args.remove("include_channel_configs")
            _message.include_channel_configs = kwargs['include_channel_configs']

        if "include_bias_voltages" in kwargs:
            unused_args.remove("include_bias_voltages")
            _message.include_bias_voltages = kwargs['include_bias_voltages']

        if "calibrated_data" in kwargs:
            unused_args.remove("calibrated_data")
            _message.calibrated_data = kwargs['calibrated_data']

        if "return_when_listening" in kwargs:
            unused_args.remove("return_when_listening")
            _message.return_when_listening = kwargs['return_when_listening']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_signal_bytes: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_signal_bytes, _message, _timeout, [], "minknow_api.data.DataService")

    def get_signal_min_max(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_signal_min_max, _message, _timeout, [], "minknow_api.data.DataService")

        unused_args = set(kwargs.keys())

        _message = GetSignalMinMaxRequest()

        if "first_channel" in kwargs:
            unused_args.remove("first_channel")
            _message.first_channel = kwargs['first_channel']
        else:
            raise ArgumentError("get_signal_min_max requires a 'first_channel' argument")

        if "last_channel" in kwargs:
            unused_args.remove("last_channel")
            _message.last_channel = kwargs['last_channel']
        else:
            raise ArgumentError("get_signal_min_max requires a 'last_channel' argument")

        if "window_size" in kwargs:
            unused_args.remove("window_size")
            _message.window_size = kwargs['window_size']
        else:
            raise ArgumentError("get_signal_min_max requires a 'window_size' argument")

        if "calibrated_data" in kwargs:
            unused_args.remove("calibrated_data")
            _message.calibrated_data = kwargs['calibrated_data']

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_signal_min_max: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_signal_min_max, _message, _timeout, [], "minknow_api.data.DataService")

    def reset_channel_states(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.reset_channel_states, _message, _timeout, [], "minknow_api.data.DataService")

        unused_args = set(kwargs.keys())

        _message = ResetChannelStatesRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to reset_channel_states: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.reset_channel_states, _message, _timeout, [], "minknow_api.data.DataService")

    def lock_channel_states(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.lock_channel_states, _message, _timeout, [], "minknow_api.data.DataService")

        unused_args = set(kwargs.keys())

        _message = LockChannelStatesRequest()

        if "channels" in kwargs:
            unused_args.remove("channels")
            _message.channels.extend(kwargs['channels'])
        else:
            raise ArgumentError("lock_channel_states requires a 'channels' argument")

        if "state_name" in kwargs:
            unused_args.remove("state_name")
            _message.state_name = kwargs['state_name']
        else:
            raise ArgumentError("lock_channel_states requires a 'state_name' argument")

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to lock_channel_states: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.lock_channel_states, _message, _timeout, [], "minknow_api.data.DataService")

    def unlock_channel_states(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.unlock_channel_states, _message, _timeout, [], "minknow_api.data.DataService")

        unused_args = set(kwargs.keys())

        _message = UnlockChannelStatesRequest()

        if "channels" in kwargs:
            unused_args.remove("channels")
            _message.channels.extend(kwargs['channels'])
        else:
            raise ArgumentError("unlock_channel_states requires a 'channels' argument")

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to unlock_channel_states: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.unlock_channel_states, _message, _timeout, [], "minknow_api.data.DataService")

    def get_live_reads(self, _iterator):
        return self._stub.get_live_reads(_iterator)

    def get_read_statistics(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_read_statistics, _message, _timeout, [], "minknow_api.data.DataService")

        unused_args = set(kwargs.keys())

        # check oneof group 'duration'
        oneof_fields = set([
            "seconds",
            "samples",
        ])

        if len(unused_args & oneof_fields) > 1:
            raise ArgumentError("get_read_statistics given multiple conflicting arguments: '{}'".format(", ".join(unused_args & oneof_fields)))

        _message = GetReadStatisticsRequest()

        if "channels" in kwargs:
            unused_args.remove("channels")
            _message.channels.extend(kwargs['channels'])

        if "seconds" in kwargs:
            unused_args.remove("seconds")
            _message.seconds = kwargs['seconds']

        if "samples" in kwargs:
            unused_args.remove("samples")
            _message.samples = kwargs['samples']

        if "read_split" in kwargs:
            unused_args.remove("read_split")
            _message.read_split = kwargs['read_split']
        else:
            raise ArgumentError("get_read_statistics requires a 'read_split' argument")

        if "no_current_statistics" in kwargs:
            unused_args.remove("no_current_statistics")
            _message.no_current_statistics = kwargs['no_current_statistics']

        if "no_chunk_statistics" in kwargs:
            unused_args.remove("no_chunk_statistics")
            _message.no_chunk_statistics = kwargs['no_chunk_statistics']

        if "required_classifications" in kwargs:
            unused_args.remove("required_classifications")
            _message.required_classifications.extend(kwargs['required_classifications'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_read_statistics: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_read_statistics, _message, _timeout, [], "minknow_api.data.DataService")

    def get_experiment_yield_info(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_experiment_yield_info, _message, _timeout, [], "minknow_api.data.DataService")

        unused_args = set(kwargs.keys())

        _message = GetExperimentYieldInfoRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_experiment_yield_info: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_experiment_yield_info, _message, _timeout, [], "minknow_api.data.DataService")
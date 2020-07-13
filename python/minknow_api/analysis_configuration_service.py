### THIS FILE IS AUTOGENERATED. DO NOT EDIT THIS FILE DIRECTLY ###
from .analysis_configuration_pb2_grpc import *
from . import analysis_configuration_pb2
from minknow_api.analysis_configuration_pb2 import *
from minknow_api._support import MessageWrapper, ArgumentError
import time
import logging

__all__ = [
    "AnalysisConfigurationService",
    "EventDetection",
    "ReadDetectionParams",
    "ReadClassificationParams",
    "ChannelStates",
    "GetAnalysisConfigurationRequest",
    "AnalysisConfiguration",
    "SetAnalysisConfigurationResponse",
    "ResetAnalysisConfigurationRequest",
    "ResetAnalysisConfigurationResponse",
    "SetAnalysisEnabledStateRequest",
    "SetAnalysisEnabledStateResponse",
    "GetChannelStatesDescRequest",
    "GetChannelStatesDescResponse",
    "GetSummaryRequest",
    "GetSummaryResponse",
    "BarcodingConfiguration",
    "AlignmentConfiguration",
    "BasecallerConfiguration",
    "SetBasecallerConfigurationRequest",
    "SetBasecallerConfigurationResponse",
    "GetBasecallerConfigurationRequest",
    "GetPoreTypeConfigurationRequest",
    "PoreTypeConfiguration",
    "SetPoreTypeConfigurationResponse",
    "WriterConfiguration",
    "SetWriterConfigurationResponse",
    "GetWriterConfigurationRequest",
    "GetReadClassificationsRequest",
    "GetReadClassificationsResponse",
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


class AnalysisConfigurationService(object):
    def __init__(self, channel):
        self._stub = AnalysisConfigurationServiceStub(channel)
        self._pb = analysis_configuration_pb2

    def get_analysis_configuration(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_analysis_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = GetAnalysisConfigurationRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_analysis_configuration: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_analysis_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def set_analysis_configuration(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.set_analysis_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = AnalysisConfiguration()

        if "event_detection" in kwargs:
            unused_args.remove("event_detection")
            _message.event_detection.CopyFrom(kwargs['event_detection'])

        if "read_detection" in kwargs:
            unused_args.remove("read_detection")
            _message.read_detection.CopyFrom(kwargs['read_detection'])

        if "read_classification" in kwargs:
            unused_args.remove("read_classification")
            _message.read_classification.CopyFrom(kwargs['read_classification'])

        if "channel_states" in kwargs:
            unused_args.remove("channel_states")
            for key, value in kwargs['channel_states'].items():
                _message.channel_states[key].CopyFrom(value)

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to set_analysis_configuration: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.set_analysis_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def reset_analysis_configuration(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.reset_analysis_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = ResetAnalysisConfigurationRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to reset_analysis_configuration: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.reset_analysis_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def set_analysis_enabled_state(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.set_analysis_enabled_state, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = SetAnalysisEnabledStateRequest()

        if "enable" in kwargs:
            unused_args.remove("enable")
            _message.enable = kwargs['enable']
        else:
            raise ArgumentError("set_analysis_enabled_state requires a 'enable' argument")

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to set_analysis_enabled_state: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.set_analysis_enabled_state, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def get_channel_states_desc(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_channel_states_desc, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = GetChannelStatesDescRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_channel_states_desc: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_channel_states_desc, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def get_summary(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_summary, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = GetSummaryRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_summary: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_summary, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def set_basecaller_configuration(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.set_basecaller_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = SetBasecallerConfigurationRequest()

        if "enable" in kwargs:
            unused_args.remove("enable")
            _message.configs.enable = kwargs['enable']

        if "config_filename" in kwargs:
            unused_args.remove("config_filename")
            _message.configs.config_filename = kwargs['config_filename']

        if "read_filtering" in kwargs:
            unused_args.remove("read_filtering")
            _message.configs.read_filtering.CopyFrom(kwargs['read_filtering'])

        if "barcoding_configuration" in kwargs:
            unused_args.remove("barcoding_configuration")
            _message.configs.barcoding_configuration.CopyFrom(kwargs['barcoding_configuration'])

        if "target_filtering" in kwargs:
            unused_args.remove("target_filtering")
            _message.configs.target_filtering.CopyFrom(kwargs['target_filtering'])

        if "alignment_configuration" in kwargs:
            unused_args.remove("alignment_configuration")
            _message.configs.alignment_configuration.CopyFrom(kwargs['alignment_configuration'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to set_basecaller_configuration: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.set_basecaller_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def get_basecaller_configuration(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_basecaller_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = GetBasecallerConfigurationRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_basecaller_configuration: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_basecaller_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def get_pore_type_configuration(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_pore_type_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = GetPoreTypeConfigurationRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_pore_type_configuration: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_pore_type_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def set_pore_type_configuration(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.set_pore_type_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        # check oneof group 'pore_type_config'
        oneof_fields = set([
            "global_pore_type",
            "channel_well_pore_types",
        ])

        if len(unused_args & oneof_fields) > 1:
            raise ArgumentError("set_pore_type_configuration given multiple conflicting arguments: '{}'".format(", ".join(unused_args & oneof_fields)))

        _message = PoreTypeConfiguration()

        if "global_pore_type" in kwargs:
            unused_args.remove("global_pore_type")
            _message.global_pore_type = kwargs['global_pore_type']

        if "channel_well_pore_types" in kwargs:
            unused_args.remove("channel_well_pore_types")
            _message.channel_well_pore_types.CopyFrom(kwargs['channel_well_pore_types'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to set_pore_type_configuration: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.set_pore_type_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def set_writer_configuration(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.set_writer_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = WriterConfiguration()

        if "read_fast5" in kwargs:
            unused_args.remove("read_fast5")
            _message.read_fast5.CopyFrom(kwargs['read_fast5'])

        if "read_fastq" in kwargs:
            unused_args.remove("read_fastq")
            _message.read_fastq.CopyFrom(kwargs['read_fastq'])

        if "read_bam" in kwargs:
            unused_args.remove("read_bam")
            _message.read_bam.CopyFrom(kwargs['read_bam'])

        if "read_protobuf" in kwargs:
            unused_args.remove("read_protobuf")
            _message.read_protobuf.CopyFrom(kwargs['read_protobuf'])

        if "sequencing_summary" in kwargs:
            unused_args.remove("sequencing_summary")
            _message.sequencing_summary.CopyFrom(kwargs['sequencing_summary'])

        if "bulk" in kwargs:
            unused_args.remove("bulk")
            _message.bulk.CopyFrom(kwargs['bulk'])

        if "report" in kwargs:
            unused_args.remove("report")
            _message.report.CopyFrom(kwargs['report'])

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to set_writer_configuration: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.set_writer_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def get_writer_configuration(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_writer_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = GetWriterConfigurationRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_writer_configuration: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_writer_configuration, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

    def get_read_classifications(self, _message=None, _timeout=None, **kwargs):
        if _message is not None:
            if isinstance(_message, MessageWrapper):
                _message = _message._message
            return run_with_retry(self._stub.get_read_classifications, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")

        unused_args = set(kwargs.keys())

        _message = GetReadClassificationsRequest()

        if len(unused_args) > 0:
            raise ArgumentError("Unexpected keyword arguments to get_read_classifications: '{}'".format(", ".join(unused_args)))

        return run_with_retry(self._stub.get_read_classifications, _message, _timeout, [], "minknow_api.analysis_configuration.AnalysisConfigurationService")
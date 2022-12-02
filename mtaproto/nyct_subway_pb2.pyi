"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.internal.extension_dict
import google.protobuf.message
import gtfs_realtime_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class TripReplacementPeriod(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ROUTE_ID_FIELD_NUMBER: builtins.int
    REPLACEMENT_PERIOD_FIELD_NUMBER: builtins.int
    route_id: builtins.str
    """The replacement period is for this route"""
    @property
    def replacement_period(self) -> gtfs_realtime_pb2.TimeRange:
        """The start time is omitted, the end time is currently now + 30 minutes for
        all routes of the A division
        """
    def __init__(
        self,
        *,
        route_id: builtins.str | None = ...,
        replacement_period: gtfs_realtime_pb2.TimeRange | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["replacement_period", b"replacement_period", "route_id", b"route_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["replacement_period", b"replacement_period", "route_id", b"route_id"]) -> None: ...

global___TripReplacementPeriod = TripReplacementPeriod

@typing_extensions.final
class NyctFeedHeader(google.protobuf.message.Message):
    """NYCT Subway extensions for the feed header"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NYCT_SUBWAY_VERSION_FIELD_NUMBER: builtins.int
    TRIP_REPLACEMENT_PERIOD_FIELD_NUMBER: builtins.int
    nyct_subway_version: builtins.str
    """Version of the NYCT Subway extensions
    The current version is 1.0
    """
    @property
    def trip_replacement_period(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TripReplacementPeriod]:
        """For the NYCT Subway, the GTFS-realtime feed replaces any scheduled
        trip within the trip_replacement_period. 
        This feed is a full dataset, it contains all trips starting 
        in the trip_replacement_period. If a trip from the static GTFS is not
        found in the GTFS-realtime feed, it should be considered as cancelled.
        The replacement period can be different for each route, so here is 
        a list of the routes where the trips in the feed replace all 
        scheduled trips within the replacement period.
        """
    def __init__(
        self,
        *,
        nyct_subway_version: builtins.str | None = ...,
        trip_replacement_period: collections.abc.Iterable[global___TripReplacementPeriod] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["nyct_subway_version", b"nyct_subway_version"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["nyct_subway_version", b"nyct_subway_version", "trip_replacement_period", b"trip_replacement_period"]) -> None: ...

global___NyctFeedHeader = NyctFeedHeader

@typing_extensions.final
class NyctTripDescriptor(google.protobuf.message.Message):
    """NYCT Subway extensions for the trip descriptor"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Direction:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _DirectionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[NyctTripDescriptor._Direction.ValueType], builtins.type):  # noqa: F821
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        NORTH: NyctTripDescriptor._Direction.ValueType  # 1
        EAST: NyctTripDescriptor._Direction.ValueType  # 2
        SOUTH: NyctTripDescriptor._Direction.ValueType  # 3
        WEST: NyctTripDescriptor._Direction.ValueType  # 4

    class Direction(_Direction, metaclass=_DirectionEnumTypeWrapper):
        """The direction the train is moving."""

    NORTH: NyctTripDescriptor.Direction.ValueType  # 1
    EAST: NyctTripDescriptor.Direction.ValueType  # 2
    SOUTH: NyctTripDescriptor.Direction.ValueType  # 3
    WEST: NyctTripDescriptor.Direction.ValueType  # 4

    TRAIN_ID_FIELD_NUMBER: builtins.int
    IS_ASSIGNED_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    train_id: builtins.str
    """The nyct_train_id is meant for internal use only. It provides an
    easy way to associated GTFS-realtime trip identifiers with NYCT rail
    operations identifier 

    The ATS office system assigns unique train identification (Train ID) to
    each train operating within or ready to enter the mainline of the
    monitored territory. An example of this is 06 0123+ PEL/BBR and is decoded
    as follows: 

    The first character represents the trip type designator. 0 identifies a
    scheduled revenue trip. Other revenue trip values that are a result of a
    change to the base schedule include; [= reroute], [/ skip stop], [$ turn
    train] also known as shortly lined service.  

    The second character 6 represents the trip line i.e. number 6 train The
    third set of characters identify the decoded origin time. The last
    character may be blank "on the whole minute" or + "30 seconds" 

    Note: Origin times will not change when there is a trip type change.  This
    is followed by a three character "Origin Location" / "Destination
    Location"
    """
    is_assigned: builtins.bool
    """This trip has been assigned to a physical train. If true, this trip is
    already underway or most likely will depart shortly. 

    Train Assignment is a function of the Automatic Train Supervision (ATS)
    office system used by NYCT Rail Operations to monitor and track train
    movements. ATS provides the ability to "assign" the nyct_train_id
    attribute when a physical train is at its origin terminal. These assigned
    trips have the is_assigned field set in the TripDescriptor.

    When a train is at a terminal but has not been given a work program it is
    declared unassigned and is tagged as such. Unassigned trains can be moved
    to a storage location or assigned a nyct_train_id when a determination for
    service is made.
    """
    direction: global___NyctTripDescriptor.Direction.ValueType
    """Uptown and Bronx-bound trains are moving NORTH.
    Times Square Shuttle to Grand Central is also northbound.

    Downtown and Brooklyn-bound trains are moving SOUTH.
    Times Square Shuttle to Times Square is also southbound.

    EAST and WEST are not used currently.
    """
    def __init__(
        self,
        *,
        train_id: builtins.str | None = ...,
        is_assigned: builtins.bool | None = ...,
        direction: global___NyctTripDescriptor.Direction.ValueType | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["direction", b"direction", "is_assigned", b"is_assigned", "train_id", b"train_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["direction", b"direction", "is_assigned", b"is_assigned", "train_id", b"train_id"]) -> None: ...

global___NyctTripDescriptor = NyctTripDescriptor

@typing_extensions.final
class NyctStopTimeUpdate(google.protobuf.message.Message):
    """NYCT Subway extensions for the stop time update"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SCHEDULED_TRACK_FIELD_NUMBER: builtins.int
    ACTUAL_TRACK_FIELD_NUMBER: builtins.int
    scheduled_track: builtins.str
    """Provides the planned station arrival track. The following is the Manhattan
    track configurations:
    1: southbound local
    2: southbound express
    3: northbound express
    4: northbound local

    In the Bronx (except Dyre Ave line)
    M: bi-directional express (in the AM express to Manhattan, in the PM
    express away).

    The Dyre Ave line is configured:
    1: southbound
    2: northbound
    3: bi-directional
    """
    actual_track: builtins.str
    """This is the actual track that the train is operating on and can be used to
    determine if a train is operating according to its current schedule
    (plan).

    The actual track is known only shortly before the train reaches a station,
    typically not before it leaves the previous station. Therefore, the NYCT
    feed sets this field only for the first station of the remaining trip.

    Different actual and scheduled track is the result of manually rerouting a
    train off it scheduled path.  When this occurs, prediction data may become
    unreliable since the train is no longer operating in accordance to its
    schedule.  The rules engine for the 'countdown' clocks will remove this
    train from all schedule stations.
    """
    def __init__(
        self,
        *,
        scheduled_track: builtins.str | None = ...,
        actual_track: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["actual_track", b"actual_track", "scheduled_track", b"scheduled_track"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["actual_track", b"actual_track", "scheduled_track", b"scheduled_track"]) -> None: ...

global___NyctStopTimeUpdate = NyctStopTimeUpdate

NYCT_FEED_HEADER_FIELD_NUMBER: builtins.int
NYCT_TRIP_DESCRIPTOR_FIELD_NUMBER: builtins.int
NYCT_STOP_TIME_UPDATE_FIELD_NUMBER: builtins.int
nyct_feed_header: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[gtfs_realtime_pb2.FeedHeader, global___NyctFeedHeader]
nyct_trip_descriptor: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[gtfs_realtime_pb2.TripDescriptor, global___NyctTripDescriptor]
nyct_stop_time_update: google.protobuf.internal.extension_dict._ExtensionFieldDescriptor[gtfs_realtime_pb2.TripUpdate.StopTimeUpdate, global___NyctStopTimeUpdate]

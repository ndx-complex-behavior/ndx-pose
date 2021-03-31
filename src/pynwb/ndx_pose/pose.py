from hdmf.utils import docval, popargs, get_docval, call_docval_func

from pynwb import register_class, TimeSeries, get_class
# from pynwb.behavior import SpatialSeries
from pynwb.core import MultiContainerInterface
from pynwb.device import Device


PoseGroupingSeries = get_class("PoseGroupingSeries", "ndx-pose")
AnimalIdentitySeries = get_class("AnimalIdentitySeries", "ndx-pose")


@register_class('PoseEstimationSeries', 'ndx-pose')
class PoseEstimationSeries(TimeSeries):
    """
    """  # TODO

    __nwbfields__ = ('reference_frame', 'confidence', 'confidence_definition')

    # custom mapper maps 'confidence' dataset > 'definition' attribute to 'confidence_definition' field here

    # TODO fill in doc
    @docval({'name': 'name', 'type': str, 'doc': ('')},  # required
            {'name': 'data', 'type': ('array_data', 'data', TimeSeries), 'shape': ((None, 2), (None, 3)),  # required
             'doc': ('')},
            {'name': 'unit', 'type': str, 'doc': ('')},  # required
            {'name': 'reference_frame', 'type': str,   # required
             'doc': 'Description defining what the zero-position (0, 0) or (0, 0, 0) is.'},
            {'name': 'confidence', 'type': ('array_data', 'data'), 'shape': (None, ), 'doc': ('')},  # required
            {'name': 'confidence_definition', 'type': str, 'doc': (''), 'default': None},
            *get_docval(TimeSeries.__init__, 'conversion', 'resolution', 'timestamps', 'starting_time', 'rate',
                        'comments', 'description', 'control', 'control_description'))
    def __init__(self, **kwargs):
        """Construct a new PoseEstimationSeries representing pose estimates for a particular body part."""
        reference_frame, confidence, confidence_definition = popargs('reference_frame', 'confidence',
                                                                     'confidence_definition', kwargs)
        call_docval_func(super().__init__, kwargs)
        self.reference_frame = reference_frame
        self.confidence = confidence
        self.confidence_definition = confidence_definition

        # TODO SpatialSeries does not allow the 'unit' argument to be different from 'meters'. This needs to be updated
        # for the inheritance to work correctly here. In the meantime, just inherit from TimeSeries


@register_class('PoseEstimation', 'ndx-pose')
class PoseEstimation(MultiContainerInterface):
    """
    """  # TODO

    __clsconf__ = [
        {
            'add': 'add_pose_estimation_series',
            'get': 'get_pose_estimation_series',
            'create': 'create_pose_estimation_series',
            'type': PoseEstimationSeries,
            'attr': 'pose_estimation_series'
        },
        {
            'add': 'add_pose_grouping_series',
            'get': 'get_pose_grouping_series',
            'create': 'create_pose_grouping_series',
            'type': PoseGroupingSeries,
            'attr': 'pose_grouping_series'
        },
        {
            'add': 'add_animal_identity_series',
            'get': 'get_animal_identity_series',
            'create': 'create_animal_identity_series',
            'type': AnimalIdentitySeries,
            'attr': 'animal_identity_series'
        },
        {
            'add': 'add_device',
            'get': 'get_devices',
            'type': Device,
            'attr': 'devices'
            # TODO prevent these from being children / add better support for links
            # may require update to HDMF to add a key 'child': False
        }
    ]

    __nwbfields__ = ('description', 'original_videos', 'labeled_videos', 'dimensions', 'scorer', 'source_software',
                     'source_software_version', 'nodes', 'edges')

    # custom mapper maps 'source_software' dataset > 'version' attribute to 'source_software_version' field here

    # TODO fill in doc
    @docval({'name': 'pose_estimation_series', 'type': ('array_data', 'data'), 'doc': (''), 'default': None},
            {'name': 'pose_grouping_series', 'type': ('array_data', 'data'), 'doc': (''), 'default': None},
            {'name': 'animal_identity_series', 'type': ('array_data', 'data'), 'doc': (''), 'default': None},
            {'name': 'name', 'type': str, 'doc': (''), 'default': 'PoseEstimation'},
            {'name': 'description', 'type': str, 'doc': (''), 'default': None},
            {'name': 'original_videos', 'type': ('array_data', 'data'), 'shape': (None, ),
             'doc': (''), 'default': None},
            {'name': 'labeled_videos', 'type': ('array_data', 'data'), 'shape': (None, ),
             'doc': (''), 'default': None},
            {'name': 'dimensions', 'type': ('array_data', 'data'), 'shape': ((None, 2)),
             'doc': (''), 'default': None},
            {'name': 'scorer', 'type': str, 'doc': (''), 'default': None},
            {'name': 'source_software', 'type': str, 'doc': (''), 'default': None},
            {'name': 'source_software_version', 'type': str, 'doc': (''), 'default': None},
            {'name': 'nodes', 'type': ('array_data', 'data'), 'doc': (''), 'default': None},
            {'name': 'edges', 'type': ('array_data', 'data'), 'doc': (''), 'default': None},
            {'name': 'devices', 'type': ('array_data', 'data'), 'doc': (''), 'default': None},
            )
    def __init__(self, **kwargs):
        """
        """  # TODO
        pose_estimation_series, description = popargs('pose_estimation_series', 'description', kwargs)
        pose_grouping_series = popargs('pose_grouping_series', kwargs)
        animal_identity_series = popargs('animal_identity_series', kwargs)
        original_videos, labeled_videos,  = popargs('original_videos', 'labeled_videos', kwargs)
        dimensions, scorer = popargs('dimensions', 'scorer', kwargs)
        source_software, source_software_version = popargs('source_software', 'source_software_version', kwargs)
        nodes, edges = popargs('nodes', 'edges', kwargs)
        devices = popargs('devices', kwargs)
        call_docval_func(super().__init__, kwargs)
        self.pose_estimation_series = pose_estimation_series
        self.pose_grouping_series = pose_grouping_series
        self.animal_identity_series = animal_identity_series
        self.description = description
        self.original_videos = original_videos
        self.labeled_videos = labeled_videos
        self.dimensions = dimensions
        self.scorer = scorer
        self.source_software = source_software
        self.source_software_version = source_software_version
        self.nodes = nodes
        self.edges = edges
        self.devices = devices

        # TODO include calibration images for 3D estimates?

        # TODO validate lengths of original_videos, labeled_videos, dimensions, and devices
        # TODO validate nodes and edges correspondence, convert edges to uint

from qiime2.plugin import Plugin, Metadata, Categorical, Str
from q2_types.sample_data import SampleData, AlphaDiversity
import q2_nc


plugin = Plugin(
    name='nested-classification',
    version=q2_nc.__version__,
    website='https://github.com/biocore/weneedtomakethis',
    package='q2_nc',
    description="what does this thingy do but be verbose",
    short_description="this does X."
)


# The semantic type SampleData requires a property.
# The only one available by default is AlphaDiversity
# so let's "use" that for now, and worry about defining
# our own property later
plugin.methods.register_function(
    function=q2_nc.samples_of_interest,
    inputs={},
    parameters={'metadata': Metadata},
    outputs=[('samples_of_interest', SampleData[AlphaDiversity])],
    input_descriptions={},
    parameter_descriptions={'metadata': 'our sample metadata'},
    output_descriptions={
        'samples_of_interest': 'sampsasdles meeting a specific criteria',
    },
    name='do stuff',
    description="do some super crazy complex",
    citations=[]
)

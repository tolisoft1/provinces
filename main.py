from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.datasets import register_url

register_url("http://gh.billchen.bid/provinces")

g = (
       Geo()
        .add_schema(maptype="China")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="China"),
        )
)
g.render("render-zh.html")

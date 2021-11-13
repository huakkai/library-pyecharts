odoo.define('library_pyecharts.view_bar', function (require) {
    "use strict";

    var BasicView = require('web.BasicView');
    var BarRenderer = require('library_pyecharts.BarRenderer');

    var viewRegistry = require('web.view_registry');

    var BarView = BasicView.extend({
        display_name: 'Bar View',
        icon: 'fa-video-camera',
        config: _.extend({}, BasicView.prototype.config, {
            Renderer: BarRenderer,
        }),
        viewType: 'bar',
    });
    viewRegistry.add('bar', BarView);
    return BarView
});

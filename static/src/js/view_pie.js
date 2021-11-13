odoo.define('library_pyecharts.view_pie', function (require) {
    "use strict";

    var BasicView = require('web.BasicView');
    var PieRenderer = require('library_pyecharts.PieRenderer');

    var viewRegistry = require('web.view_registry');

    var PieView = BasicView.extend({
        display_name: 'Pie View',
        icon: 'fa-video-camera',
        config: _.extend({}, BasicView.prototype.config, {
            Renderer: PieRenderer,
        }),
        viewType: 'pie',
    });
    viewRegistry.add('pie', PieView);
    return PieView
});

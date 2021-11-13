odoo.define('library_pyecharts.BarRenderer', function (require) {
    'use strict';

    var AbstractRenderer = require('web.AbstractRenderer');


    return AbstractRenderer.extend({


        template: 'BarTemplate',


        _consoleBtn: function() {
            console.log(this.state.model);

        },

        init: function(parent, data){
            return this._super.apply(this, arguments);
        },

        start: function(){
            this._consoleBtn();
            var model = this.state.model;
            $(document).ready(function() {
                $.ajax({
                    type: "GET",
                    url: "/pyecharts",
                    data: {model: model, etype: "Bar"},
                    dataType: 'json',
                    success: function (result) {
                        var echartsData = result.echarts_data;
                        var bar = document.getElementById("bar");
                        var chart = echarts.init(bar, 'shine', {renderer: 'canvas'});
                        chart.setOption(echartsData);
                    },
                    error: function (request) {
                        console.log("error")
                    },
                });
            });
            return true;
        },
    });

});

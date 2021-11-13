odoo.define('library_pyecharts.PieRenderer', function (require) {
    'use strict';

    var AbstractRenderer = require('web.AbstractRenderer');


    return AbstractRenderer.extend({


        template: 'PieTemplate',


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
                    data: {model: model, etype: "Pie"},
                    dataType: 'json',
                    success: function (result) {
                        var echartsData = result.echarts_data;
                        var pie = document.getElementById("pie");
                        var chart = echarts.init(pie, 'shine', {renderer: 'canvas'});
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

L.Control.Layers.prototype._addItem = function(obj) {
        var label = document.createElement('label'),
            input,
            checked = this._map.hasLayer(obj.layer);

        if (obj.overlay) {
            input = document.createElement('input');
            input.type = 'checkbox';
            input.className = 'leaflet-control-layers-selector';
            input.defaultChecked = checked;
        }
        else {
            input = this._createRadioElement('leaflet-base-layers', checked);
        }

        input.layerId = L.stamp(obj.layer);

        L.DomEvent.on(input, 'click', this._onInputClick, this);

        var name = document.createElement('span');
        name.innerHTML = ' ' + obj.name;

        label.appendChild(input);
        label.appendChild(name);
        label.className = obj.overlay ? "checkbox" : "radio";
        var container = obj.overlay ? this._overlaysList : this._baseLayersList;
        container.appendChild(label);

        return label;
    }
var m = L.map("map", {
        zoomControl: false
    });
    if (!location.hash) {
        m.setView([44.3967,8.6732], 3);
    }
    m.addHash();
    
    // create the tile layer with correct attribution
	var url='http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
	var attributionText='Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors';


    var optionsObject = {
        attribution: attributionText    }

    var mq = L.tileLayer(url, optionsObject);
    var watercolor = L.tileLayer('http://{s}.tile.stamen.com/terrain/{z}/{x}/{y}.jpg', {
        attribution: 'Map tiles by <a href="http://stamen.com">Stamen Design</a>, <a href="http://creativecommons.org/licenses/by/3.0">CC BY 3.0</a> &mdash; Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'
    })
    mq.addTo(m);
    var lc = L.control.layers({
        "Stamen terrain": watercolor,
        "OpenstreetMap": mq
    }).addTo(m);
    //make the map
    var options = {
        onEachFeature: function(feature, layer) {
            if (feature.properties) {
                layer.bindPopup(Object.keys(feature.properties).map(function(k) {
                    if(k === '__color__'){
                        return;
                    }
                    return k + ": " + feature.properties[k];
                }).join("<br />"), {
                    maxHeight: 200
                });
            }
        },
        style: function(feature) {
            return {
                opacity: 1,
                fillOpacity: 0.5,
                radius: 6,
                color: feature.properties.__color__
            }
        },
        pointToLayer: function(feature, latlng) {
            return L.circleMarker(latlng, {
                opacity: 1,
                fillOpacity: 0.5,
                color: feature.properties.__color__
            });
        }
    };

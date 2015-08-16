var do_svg = function(svg_source, container) {
    var SVG_out = "";
    var input = {
        img_out: function(img) {
            SVG_out += img;
            container.innerHTML = SVG_out;
        },
        errmsg: function(message, line_number, column_number) {
            console.error([message, line_number, column_number]);
        },
        read_file: function(file) {
            // we don't support includes
            return "";
        }
    };

    var abc = new Abc(input);
    abc.tosvg("tune", svg_source);
};
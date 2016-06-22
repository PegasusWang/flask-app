(function() {
  var clearSelectbox;

  clearSelectbox = function(selectbox) {
    var i, j, len, ref, results;
    len = selectbox.options.length;
    results = [];
    for (i = j = 0, ref = len; 0 <= ref ? j < ref : j > ref; i = 0 <= ref ? ++j : --j) {
      results.push(selectbox.remove(0));
    }
    return results;
  };

  $(document).ready(function() {
    var s, sel;
    s = "";
    if (s) {
      console.log('hehe');
    }
    sel = $('#selLocation').get(0);
    return clearSelectbox(sel);
  });

}).call(this);

//# sourceMappingURL=t.js.map

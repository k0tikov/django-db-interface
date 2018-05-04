
var matches = new Bloodhound({
  datumTokenizer: Bloodhound.tokenizers.obj.whitespace('q'),
  queryTokenizer: Bloodhound.tokenizers.whitespace,
  prefetch: 'tables_found.json?q=%QUERY',
  remote: {
    url: 'tables_found.json?q=%QUERY',
    wildcard: '%QUERY'
  }
});

$('#typeahead').typeahead(null, {
  name: 'matches',
  displayKey: 'q',
  source: matches.ttAdapter()
});
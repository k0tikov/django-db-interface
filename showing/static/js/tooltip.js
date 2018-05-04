/* increasing size of table */




            /*$(document).ready(function (){*/
                $
                
                var tbl = document.getElementById('gl-table');
                var MyHint = document.getElementById('column-tooltip');

                tbl.onmouseover = function(e) {
                    e = e || event;
                    var el = e.target || e.srcElement;
                    if (el.tagName.toUpperCase() != 'DIV') {return;}

                    var box = el.getBoundingClientRect();
                    MyHint.style.left = box.left - 1 + 'px'; //width
                    MyHint.style.top = box.top - 55 + 'px';
                    MyHint.innerHTML = el.innerHTML;
                    MyHint.style.display = 'block';
                    if (MyHint.offsetWidth < el.offsetWidth) {MyHint.style.display = 'none';}
                    }

                MyHint.onmouseout = function(e) {
                        e = e || event;
                        var el = e.target || e.srcElement;
                        MyHint.style.display = 'none';
                    }
                    





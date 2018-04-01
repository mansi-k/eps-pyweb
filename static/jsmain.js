function sayHello() {
   alert("Hello World");
}

function tsformat(){
   	// Do your stuff here
	var sts = document.getElementById('ixs').value;
	var newsts = new Date(sts);
	var sday = newsts.getDate();
	var smonth = newsts.getMonth();
	var syear = newsts.getFullYear();
	var shrs = newsts.getHours();
	var smin = newsts.getMinutes();
	var nsts = sday+'-'+smonth+'-'+syear+' '+shrs+':'+smin+':00';
	document.getElementById('ixs').type='text'; 
	document.getElementById('ixs').value=nsts ; 
	var ets = document.getElementById('ixe').value;
	var newets = new Date(ets);
	var eday = newets.getDate();
	var emonth = newets.getMonth();
	var eyear = newets.getFullYear();
	var ehrs = newets.getHours();
	var emin = newets.getMinutes();
	var nets = eday+'-'+emonth+'-'+eyear+' '+ehrs+':'+emin+':00';
	document.getElementById('ixe').type='text'; 
	document.getElementById('ixe').value=nets ;
	return true;
}

/*
function sortexs(obj) {
    var months = 'January___February__March_____April_____May_______June______July______August____September_October___November__December__'
    var tp = $(obj).closest('.tab-pane').attr('id');
    var $table = $('#'+tp+'table');
    var rows = $table.find('tr').not(':first').get();
    //alert(Date.parse($(rows[1]).find("td:nth-child(4)").html()))
    if($(obj).val()=='old') {
        rows.sort(function(a, b) {
            var d1 = $(a).find("td:nth-child(4)").html();
            var d2 = $(b).find("td:nth-child(4)").html();
            var d1m = months.indexOf(d1.split(' ',1)[0]) / 10 + 1;
            var d2m = months.indexOf(d2.split(' ',1)[0]) / 10 + 1;
            var d1y = d1.split(', ',1)[1];
            var d2y = d2.split(', ',1)[1];
            //alert(d1.split(' ',2)[1])
            var d1d = d1.split(' ',2)[1];
            var d2d = d2.split(' ',2)[1];
            var keyA = new Date(d1y,d1m,d1d)
            alert(d1m)
            var keyB = new Date(d2y,d2m,d2d)
            if (keyA < keyB) return 1;
            if (keyA > keyB) return -1;
            return 0;
        });
    }
    else {
        rows.sort(function(a, b) {
            var keyA = Date.parse($(a).find("td:nth-child(4)").html())
            var keyB = Date.parse($(a).find("td:nth-child(4)").html())
            if (keyA > keyB) return 1;
            if (keyA < keyB) return -1;
            return 0;
        });
    }
    $.each(rows, function(index, row) {
        $table.children('tbody').append(row);
    });
}
*/

function sortexs(obj) {
    var tp = $(obj).closest('.tab-pane').attr('id');
    var $table = $('#'+tp+'table');
    var rows = $table.find('tr').not(':first').get();
    if($(obj).val()=='old') {
        rows.sort(function(a, b) {
            var keyA = Date.parse($(a).find("td:nth-child(4)").html())
            var keyB = Date.parse($(b).find("td:nth-child(4)").html())
            if (keyA < keyB) return 1;
            if (keyA > keyB) return -1;
            return 0;
        });
    }
    else {
        rows.sort(function(a, b) {
            var keyA = Date.parse($(a).find("td:nth-child(4)").html())
            var keyB = Date.parse($(a).find("td:nth-child(4)").html())
            if (keyA > keyB) return 1;
            if (keyA < keyB) return -1;
            return 0;
        });
    }
    $.each(rows, function(index, row) {
        $table.children('tbody').append(row);
    });
}

function catexs(obj) {
    var cat = $(obj).val();
    var tp = $(obj).closest('.tab-pane').attr('id');
    var $table = $('#'+tp+'table');
    if(cat=='All')
        var rows = $table.find('tr').not(':first').show();
    else {
            var rows = $table.find('tr').not(':first').hide();
            $(rows).each(function() {
                if($(this).find("td:nth-child(2)").html()==cat)
                    $(this).show();
            });
        }
}

function searchexs(obj) {
    var srch = $(obj).val();
    var tp = $(obj).closest('.tab-pane').attr('id');
    var $table = $('#'+tp+'table');
    var rows = $table.find('tr').not(':first').get();
    $.each(rows, function(index, row) {
        $(row).hide();
        if($(row).attr('aria-controls').indexOf(srch) != -1)
            $(row).show()
    });
}

function cityexs(obj) {
    var city = $(obj).val();
    var tp = $(obj).closest('.tab-pane').attr('id');
    var $table = $('#'+tp+'table');
    if(city=='all')
        var rows = $table.find('tr').not(':first').show();
    else {
            var rows = $table.find('tr').not(':first').hide();
            $.each(rows, function(index, row) {
                if($(row).find("td:nth-child(3)").html().indexOf(city) != -1)
                    $(row).show();
            });
        }
}
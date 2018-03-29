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

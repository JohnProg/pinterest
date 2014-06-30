var app = angular.module('myApp', []);
app.config(function($interpolateProvider){
	$interpolateProvider.startSymbol('{[{');
	$interpolateProvider.endSymbol('}]}');
});
app.controller('mainCtrl', function($scope, mainService){
	mainService.getListOfItems
		.then(function(resp){
			$scope.items = resp.data;
		});
	$scope.name = 'dasds';
	$scope.getMoreItemDetail = function(ind){
		$scope.currentItem = $scope.items[ind];
		angular.element('#mainModal').modal('show');
	};
	$scope.tabItems = [
		{name: "Imagenes"},
		{name: "Materiales"},
		{name: "Elaboracion"}
	];
	$scope.showTab = function(ind){
		debugger
		angular.element('.tab-items > li').removeClass('active-tab-item');
		angular.element('.tab-items > li').eq(ind).addClass('active-tab-item');
	};
});

app.factory('mainService', function($http){
	return {
		getListOfItems: $http.get('./static/js/scrapy.json')
	}
});
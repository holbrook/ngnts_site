'use strict';

/**
 * @ngdoc function
 * @name ngntsApp.controller:MessageCtrl
 * @description
 * # MessageCtrl
 * Controller of the ngntsApp
 */
angular.module('ngntsApp')
  .controller('MsgDetailCtrl', function ($scope, $routeParams, $http) {
    console.log("msgDetail controller");
    $scope.code = $routeParams.code;

    $http({url:"data/messages/"+$scope.code+".json"})
      .success(function(data, status, headers, config){
          $scope.message = data;
          for(var x in $scope.message.request){
            var item = $scope.message.request[x];
            if (item['type'].indexOf("N") >= 0){
              if (item['type'].indexOf(".") >=0 ){
                item['ride_type'] = 'Doub';
              }
              else{
               item['ride_type'] = 'Int';
              }
            }else{
              if (item['type'] == 'C1'){
                item['ride_type'] = 'Char';
              }
              else{
                item['ride_type'] = 'Str';
              }
            }


          }
      })
      .error(function(data, status, headers, config){
                // alert("error");
      });


  });

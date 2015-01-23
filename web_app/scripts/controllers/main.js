'use strict';

/**
 * @ngdoc function
 * @name ngntsApp.controller:MainCtrl
 * @description
 * # MainCtrl
 * Controller of the ngntsApp
 */
angular.module('ngntsApp')
  .controller('MainCtrl', function ($rootScope, $scope) {
    console.log("main controller");

    //定义索引
    var lunr_idx = lunr(function () {
        this.field('code')
        this.field('name')
    })


    var msg_count = 0;
    for (var m in $scope.idx.messages){
        msg_count++;
        var x = $scope.idx.messages[m];

        //添加索引
        lunr_idx.add({"code":x.code, "name":x.name});
    //搜索
    console.log(lunr_idx.search("522"));
    }

    $scope.msg_count = msg_count;

    var app_count = 0;
    for (var a in $scope.idx.apps){
        app_count++;
    }
    $scope.app_count = app_count;

    var scope_count = 0;
    for (var a in $scope.idx.scopes){
        scope_count++;
    }
    $scope.scope_count = scope_count;

    var dict_count = 0;

    for (var a in $scope.idx.dicts){
        dict_count++;
    }
    $scope.dict_count = dict_count;

    // $scope.idx = $rootScope.idx;


  });

angular.module('bootstrapextracomponentsDropdown', ['servoy']).directive('bootstrapextracomponentsDropdown', function() {
		return {
			restrict: 'E',
			scope: {
				model: '=svyModel',
				api: "=svyApi",
				handlers: "=svyHandlers",
				svyServoyapi: "="
			},
			controller: function($scope, $element, $attrs, $window,$utils) {
				$scope.status = {
					isopen: false
				};
				
				if (!$scope.model.menuItems) {
					$scope.model.menuItems = [];
				}
				
				function getItem(event) {
					try {
						var itemId = event.target.getAttribute('data-menu-item-id');
						var itemClicked;
						if (!itemId) {
							console.log('dropdown item "' + event.target.text + '" has no itemId');
						} else {
							for (var i = 0; i < $scope.model.menuItems.length; i++) {
								var menuItem = $scope.model.menuItems[i];
								if (menuItem.itemId == itemId || menuItem.text == itemId) {
									itemClicked = menuItem;
									break;
								}
							}
							if (itemClicked) {
								itemClicked.displayValue = event.target.value;
							}
							return itemClicked;
						}
					} catch (e) {
						console.log('Error when trying to figure out dropdown itemId: ' + e.message);
					}
					return null;
				}
				
				function createItemArg(item) {
					var itemText = item.text;
					if (item.displayValue) {
						itemText = item.displayValue;
					}
					return { itemId: item.itemId ? item.itemId : null, text: itemText ? itemText : null, userData: item.userData ? item.userData : null };
				}
				
				$scope.dropDownClicked = function(event) {
					var element = event.currentTarget;
					var ul = $('#button-dropdown-ul-' + $scope.model.svyMarkupId);
					if (element && ul) {
						var boundingRect = element.getBoundingClientRect();
						ul.attr('style', 'position: fixed; left: ' + boundingRect.left + 'px; top: ' + (boundingRect.top + boundingRect.height + 2) + 'px;')
					}
					if (event.target.id === 'button-dropdown-' + $scope.model.svyMarkupId) {
						//click on the menu caret on a split button or on a non split button
						return;
					}
					if (event.target.id === 'button-' + $scope.model.svyMarkupId) {
						//click on the button (not the menu caret) of a split button
						if ($scope.handlers.onAction){
							$scope.handlers.onAction(event);
						}
						return;
					}
					var li = $(event.target).closest('li');
					if (li && li.hasClass('disabled')) {
						//disabled entry
						return;
					}
					var itemClicked = getItem(event);
					if (itemClicked && itemClicked.onAction) {
						var jsEvent = $utils.createJSEvent(event,'action');
						$window.executeInlineScript(itemClicked.onAction.formname, itemClicked.onAction.script, [jsEvent, createItemArg(itemClicked)]);
					} else if (itemClicked && $scope.handlers.onMenuItemSelected) {
						$scope.handlers.onMenuItemSelected(event, createItemArg(itemClicked));
					}
				}
			},
			templateUrl: 'bootstrapextracomponents/dropdown/dropdown.html'
		};
	})
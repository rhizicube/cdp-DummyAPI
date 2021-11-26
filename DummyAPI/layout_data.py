LAYOUT_ID_100 = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "layout_id_100",
                    "layout_type": "health",
                    "layout_title": "No Title",
                    "layout_description": "Track and Check if all connectors working properly",
                    "side_component_tab_id": "layout_tab_id_200",
                    "side_component_type": "button",
                    "side_component_name": "Connector's Health",
                    "side_component_action_initiate": "layout_id_106",
                    "side_component_action_performed": "overlay_layout",
                    "tabs": {
                        "layout_tab_id_200": {
                            "layout_tab_id": "layout_tab_id_200",
                            "layout_tab_name": "Data Metrics",
                            "layout_tab_type": "card-graph",
                            "data_api": "",
                            "card_action": "",
                            "keep_me_notified": True,
                            "is_dynamic": False,
                            "card_metric_ids": [
                                "metric_layout_300",
                                "metric_layout_301"
                            ],
                            "graph_metric_ids": [
                                "metric_layout_302",
                                "metric_layout_303"
                            ],
                            "table_metric_ids": None,
                            "information_metric_ids": None,
                            "filter_ids": None,
                            "metadata": None
                        },
                        "layout_tab_id_201": {
                            "layout_tab_id": "layout_tab_id_201",
                            "layout_tab_name": "Connectors",
                            "layout_tab_type": "connector",
                            "data_api": "/connector_data",
                            "card_action": "",
                            "keep_me_notified": False,
                            "is_dynamic": False,
                            "card_metric_ids": None,
                            "graph_metric_ids": None,
                            "table_metric_ids": None,
                            "information_metric_ids": None,
                            "filter_ids": None,
                            "metadata": None
                        }
                    }
                }
            }

LAYOUT_ID_106 = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "layout_id_106",
                    "layout_type": "connectors-health",
                    "layout_title": "All connectors data health",
                    "layout_description": "",
                    "side_component_tab_id": "",
                    "side_component_type": "",
                    "side_component_name": "",
                    "side_component_action_initiate": "",
                    "side_component_action_performed": "",
                    "tabs": {
                        "layout_tab_id_202": {
                            "layout_tab_id": "layout_tab_id_202",
                            "layout_tab_name": "",
                            "layout_tab_type": "card-graph",
                            "data_api": "",
                            "card_action": "",
                            "keep_me_notified": False,
                            "is_dynamic": True,
                            "card_metric_ids": None,
                            "graph_metric_ids": [
                                "metric_layout_304",
                                "metric_layout_304",
                                "metric_layout_304",
                                "metric_layout_304",
                                "metric_layout_304",
                                "metric_layout_304",
                                "metric_layout_304",
                                "metric_layout_304"
                            ],
                            "table_metric_ids": None,
                            "information_metric_ids": None,
                            "filter_ids": [
                                "filter_id_501",
                                "filter_id_508",
                                "filter_id_509"
                            ],
                            "metadata": [
                                {
                                    "connection_status": "operational",
                                    "connection_type": "ingress",
                                    "connector_repository_group_name": "Servers",
                                    "custom_connection_name": "Shopify",
                                    "description": "Copy and paste the JS tags on your website",
                                    "display_image_url": "shopify.svg",
                                    "id": "101",
                                    "type": "connector"
                                },
                                {
                                    "connection_status": "operational",
                                    "connection_type": "egress",
                                    "connector_repository_group_name": "Storage",
                                    "custom_connection_name": "Amazon S3",
                                    "description": "Feed data to your custom server",
                                    "display_image_url": "aws_s3.svg",
                                    "id": "102",
                                    "type": "connector"
                                },
                                {
                                    "connection_status": "operational",
                                    "connection_type": "ingress",
                                    "connector_repository_group_name": "Mobile App",
                                    "custom_connection_name": "Android SDK",
                                    "description": "Integrate SDK with your android app",
                                    "display_image_url": "android.svg",
                                    "id": "103",
                                    "type": "connector"
                                },
                                ###############################################################################################
                                {
                                    "connection_status": "blocked",
                                    "connection_type": "ingress",
                                    "connector_repository_group_name": "Servers",
                                    "custom_connection_name": "Shopify",
                                    "description": "Copy and paste the JS tags on your website",
                                    "display_image_url": "shopify.svg",
                                    "id": "104",
                                    "type": "connector"
                                },
                                {
                                    "connection_status": "operational",
                                    "connection_type": "egress",
                                    "connector_repository_group_name": "Storage",
                                    "custom_connection_name": "Amazon S3",
                                    "description": "Feed data to your custom server",
                                    "display_image_url": "aws_s3.svg",
                                    "id": "105",
                                    "type": "connector"
                                },
                                {
                                    "connection_status": "blocked",
                                    "connection_type": "ingress",
                                    "connector_repository_group_name": "Mobile App",
                                    "custom_connection_name": "Android SDK",
                                    "description": "Integrate SDK with your android app",
                                    "display_image_url": "android.svg",
                                    "id": "106",
                                    "type": "connector"
                                },
                                {
                                    "connection_status": "blocked",
                                    "connection_type": "egress",
                                    "connector_repository_group_name": "Servers",
                                    "custom_connection_name": "Shopify",
                                    "description": "Copy and paste the JS tags on your website",
                                    "display_image_url": "shopify.svg",
                                    "id": "107",
                                    "type": "connector"
                                },
                                {
                                    "connection_status": "blocked",
                                    "connection_type": "egress",
                                    "connector_repository_group_name": "Storage",
                                    "custom_connection_name": "Amazon S3",
                                    "description": "Feed data to your custom server",
                                    "display_image_url": "aws_s3.svg",
                                    "id": "108",
                                    "type": "connector"
                                }
                                ##################################################################################################
                            ]
                        }
                    }
                }
            }

LAYOUT_ID_107 = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "layout_id_107",
                    "layout_type": "errors",
                    "layout_title": "Issue List",
                    "layout_description": "View and Diagnose via some issue know to us",
                    "side_component_tab_id": "",
                    "side_component_type": "",
                    "side_component_name": "",
                    "side_component_action_initiate": "",
                    "side_component_action_performed": "",
                    "tabs": {
                        "layout_tab_id_203": {
                            "layout_tab_id": "layout_tab_id_203",
                            "layout_tab_name": "Known Issues",
                            "layout_tab_type": "information",
                            "data_api": "",
                            "card_action": "",
                            "keep_me_notified": False,
                            "is_dynamic": False,
                            "card_metric_ids": None,
                            "graph_metric_ids": None,
                            "table_metric_ids": None,
                            "information_metric_ids": [
                                "metric_layout_305"
                            ],
                            "filter_ids": None,
                            "metadata": [
                                {
                                    "connection_status": "operational",
                                    "connection_type": "egress",
                                    "connector_repository_group_name": "Storage",
                                    "custom_connection_name": "Amazon S3",
                                    "description": "Feed data to your custom server",
                                    "display_image_url": "aws_s3.svg",
                                    "id": "102",
                                    "original_id": "metric_id_404",
                                    "original_type": "metrics",
                                    "type": "connector"
                                }
                            ]
                        },
                        "layout_tab_id_204": {
                            "layout_tab_id": "layout_tab_id_204",
                            "layout_tab_name": "Error Logs",
                            "layout_tab_type": "table",
                            "data_api": "",
                            "card_action": "",
                            "keep_me_notified": False,
                            "is_dynamic": False,
                            "card_metric_ids": None,
                            "graph_metric_ids": None,
                            "table_metric_ids": [
                                "metric_layout_306"
                            ],
                            "information_metric_ids": None,
                            "filter_ids": None,
                            "metadata": [
                                {
                                    "connection_status": "operational",
                                    "connection_type": "egress",
                                    "connector_repository_group_name": "Storage",
                                    "custom_connection_name": "Amazon S3",
                                    "description": "Feed data to your custom server",
                                    "display_image_url": "aws_s3.svg",
                                    "id": "102",
                                    "original_id": "metric_id_404",
                                    "original_type": "metrics",
                                    "type": "connector"
                                }
                            ]
                        }
                    }
                }
            }

LAYOUT_ID_108 ={
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "layout_id_108",
                    "layout_type": "customer",
                    "layout_title": "Customer dashboard",
                    "layout_description": "Customer dashboard shows your CDPs customer insights",
                    "side_component_tab_id": "",
                    "side_component_type": "",
                    "side_component_name": "",
                    "side_component_action_initiate": "",
                    "side_component_action_performed": "",
                    "tabs": {
                        "layout_tab_id_205": {
                            "layout_tab_id": "layout_tab_id_205",
                            "layout_tab_name": "Customer's overview",
                            "layout_tab_type": "card-graph",
                            "data_api": "",
                            "card_action": "",
                            "keep_me_notified": False,
                            "is_dynamic": False,
                            "card_metric_ids": [
                                "metric_layout_307",
                                "metric_layout_308",
                                "metric_layout_309",
                                "metric_layout_310"
                            ],
                            "graph_metric_ids": [
                                "metric_layout_311",
                                "metric_layout_312",
                                "metric_layout_313",
                                "metric_layout_314"
                            ],
                            "table_metric_ids": None,
                            "information_metric_ids": None,
                            "filter_ids": None,
                            "metadata": None
                        },
                        "layout_tab_id_206": {
                            "layout_tab_id": "layout_tab_id_206",
                            "layout_tab_name": "All Customers",
                            "layout_tab_type": "customer_table",
                            "data_api": "",
                            "card_action": "",
                            "keep_me_notified": False,
                            "is_dynamic": False,
                            "card_metric_ids": None,
                            "graph_metric_ids": None,
                            "table_metric_ids": [
                                "metric_layout_315"
                            ],
                            "information_metric_ids": None,
                            "filter_ids": None,
                            "metadata": None
                        }
                        
                    }
                }
            }

LAYOUT_ID_109 = {
                "code": 200,
                "msg": "Success",
                "status": "success",
                "data": {
                    "layout_id": "layout_id_109",
                    "layout_type": "customer",
                    "layout_title": "",
                    "layout_description": "",
                    "side_component_tab_id": "",
                    "side_component_type": "",
                    "side_component_name": "",
                    "side_component_action_initiate": "",
                    "side_component_action_performed": "",
                    "tabs": {
                        "layout_tab_id_207": {
                            "layout_tab_id": "layout_tab_id_207",
                            "layout_tab_name": "Overview",
                            "layout_tab_type": "card-graph",
                            "data_api": "",
                            "card_action": "",
                            "keep_me_notified": False,
                            "is_dynamic": False,
                            "card_metric_ids": [
                                "metric_layout_316",
                                "metric_layout_317",
                                "metric_layout_318",
                                "metric_layout_319"
                            ],
                            "graph_metric_ids":None,
                            "table_metric_ids": None,
                            "information_metric_ids": None,
                            "filter_ids": None,
                            "metadata": None
                        },
                        "layout_tab_id_208": {
                            "layout_tab_id": "layout_tab_id_208",
                            "layout_tab_name": "Channel",
                            "layout_tab_type": "card-graph",
                            "data_api": "",
                            "card_action": "",
                            "keep_me_notified": False,
                            "is_dynamic": False,
                            "card_metric_ids": [
                                "metric_layout_320",
                                "metric_layout_321"
                            ],
                            "graph_metric_ids": None,
                            "table_metric_ids":None,
                            "information_metric_ids": None,
                            "filter_ids": None,
                            "metadata": None
                        },
                        "layout_tab_id_209": {
                            "layout_tab_id": "layout_tab_id_209",
                            "layout_tab_name": "Revenue",
                            "layout_tab_type": "card-graph",
                            "data_api": "",
                            "card_action": "",
                            "keep_me_notified": False,
                            "is_dynamic": False,
                            "card_metric_ids": [
                                "metric_layout_322",
                                "metric_layout_323",
                                "metric_layout_324",
                                "metric_layout_325"
                            ],
                            "graph_metric_ids": [
                                "metric_layout_326",
                            ],
                            "table_metric_ids":None,
                            "information_metric_ids": None,
                            "filter_ids": None,
                            "metadata": None
                        },
                        "layout_tab_id_210": {
                            "layout_tab_id": "layout_tab_id_210",
                            "layout_tab_name": "Product metrics",
                            "layout_tab_type": "card-graph",
                            "data_api": "",
                            "card_action": "",
                            "keep_me_notified": False,
                            "is_dynamic": False,
                            "card_metric_ids": [
                                "metric_layout_327",
                                "metric_layout_328"
                            ],
                            "graph_metric_ids": [
                                "metric_layout_329",
                            ],
                            "table_metric_ids":None,
                            "information_metric_ids": None,
                            "filter_ids": None,
                            "metadata": None
                        },
                        
                    }
                }
            }
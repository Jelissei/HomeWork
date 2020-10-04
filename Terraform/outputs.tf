output "endpoint" {
	value = "${azurerm_subnet.subnet.service_endpoints}"
}

output "user_name" {
	value = "${azurerm_sql_server.main.administrator_login}"
}

output "password" {
	value = "${azurerm_sql_server.main.administrator_login_password}"
}
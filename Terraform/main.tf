provider "azurerm" {
  subscription_id = "${var.subscription}"
  version = "2.4.0"
  features {}
}

resource "azurerm_resource_group" "main" {
  name = "${var.resName}"
  location = "${var.region}"
}

resource "azurerm_virtual_network" "vnet" {
  name                = "${var.vnetName}"
  address_space       = ["10.1.0.0/24"]
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
}

resource "azurerm_subnet" "subnet" {
  name                 = "${var.subnetName}"
  resource_group_name  = azurerm_resource_group.main.name
  virtual_network_name = azurerm_virtual_network.vnet.name
  address_prefix       = "${var.addressPrefix}"
  service_endpoints    = ["Microsoft.Sql"]
}

resource "azurerm_sql_server" "main" {
  name = "${var.resName}"
  resource_group_name = azurerm_resource_group.main.name
  location = "${var.region}"
  version = "12.0"
  administrator_login = "${var.login}"
  administrator_login_password = "${var.password}"
}

resource "azurerm_sql_database" "main" {
  name = "${var.resName}"
  resource_group_name = azurerm_resource_group.main.name
  location = "${var.region}"
  server_name = azurerm_sql_server.main.name
}
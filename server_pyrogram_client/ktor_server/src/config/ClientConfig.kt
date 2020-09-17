package com.openproject.config

data class ClientConfig(
  public val app_api_id: String,
  public val app_api_hash: String,
  public val name: String,
  public val test_configuration: String,
  public val product_configuration: String,
  public val trigger_username: String,
  public val message_on_trigger: String
)

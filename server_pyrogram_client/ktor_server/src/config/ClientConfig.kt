package com.openproject.config


import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.encodeToJsonElement
import java.io.FileInputStream


data class ClientConfig(
  public val app_api_id: String,
  public val app_api_hash: String,
  public val name: String,
  public val test_configuration: String,
  public val product_configuration: String,
  public val trigger_username: String,
  public val message_on_trigger: String
) {
    companion object {
        suspend fun loadDataFromJsonFile(path: String = "../src/config/client.json") {

            val contents = withContext(Dispatchers.IO) {
                FileInputStream(path).use {
                    it.readBytes()
                }

            }
            val json = Json.encodeToJsonElement(contents)
            println(json)


        }


    }
}



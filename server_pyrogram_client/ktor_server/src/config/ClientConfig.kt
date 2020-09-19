package com.openproject.config


import kotlinx.serialization.json.Json
import kotlinx.serialization.Serializable
import kotlinx.serialization.decodeFromString
import java.io.File


@Serializable
data class ClientConfig(
   val app_api_id: String,
   val app_api_hash: String,
   val name: String,
   val test_configuration: String,
   val product_configuration: String,
   val trigger_username: String,
   val response_message_on_trigger: String
) {
    companion object {
       fun loadDataFromJsonFile(path: String = "../src/config/client.json"): ClientConfig {
            val contents = File(path).readText()
            return Json.decodeFromString(string = contents)
        }
    }
}





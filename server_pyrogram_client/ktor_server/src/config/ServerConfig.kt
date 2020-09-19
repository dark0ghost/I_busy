package com.openproject.config

import kotlinx.serialization.Serializable
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.json.Json
import java.io.File

@Serializable
data class ServerConfig(
    val host: String,
    val port: Int,
    val path_to_html: String,
    val support_ssl: Boolean,
    val path_to_ssl: String,
){
    companion object {
         fun loadDataFromJsonFile(path: String = "../src/config/server.json"): ServerConfig {
             val contents = File(path).readText()
             return Json.decodeFromString(string = contents)
        }
    }
}
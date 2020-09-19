package com.openproject.config

import kotlinx.serialization.Serializable
import kotlinx.serialization.decodeFromString
import kotlinx.serialization.json.Json
import java.io.File

@Serializable
data class DataBaseConfig(
    val host: String,
    val port: Int,
    val postgres_user: String,
    val postgres_password: String,
    val need_update: Boolean
){
    companion object {
       fun loadDataFromJsonFile(path: String = "../src/config/database.json"): DataBaseConfig {
           val contents = File(path).readText()
           return Json.decodeFromString(string = contents)
        }
    }
}
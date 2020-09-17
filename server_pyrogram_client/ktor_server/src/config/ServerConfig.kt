package com.openproject.config

data class ServerConfig(
    val host: String,
    val port: Int,
    val path_to_html: String,
    val support_ssl: Boolean,
    val path_to_ssl: String,
)
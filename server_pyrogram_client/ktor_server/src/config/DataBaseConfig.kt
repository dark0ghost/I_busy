package com.openproject.config

data class DataBaseConfig(
    val host: String,
    val port: Int,
    val postgres_user: String,
    val postgres_password: String,
    val need_update: Boolean
)
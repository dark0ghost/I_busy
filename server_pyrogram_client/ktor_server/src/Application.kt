package com.openproject

import com.openproject.config.Config
import com.openproject.lib.loadConfig
import io.ktor.application.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*


fun main(args: Array<String>): Unit {
    val config: Config = loadConfig() as Config
    embeddedServer(Netty, port = config.server.port) {
        routing {
            get(path = "/api/command/"){

            }
            get(path = "/api/"){

            }
        }
    }.start(wait = true)
}




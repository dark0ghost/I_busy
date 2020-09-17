package com.openproject

import io.ktor.application.*
import io.ktor.response.*
import io.ktor.request.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*

//fun main(args: Array<String>): Unit = io.ktor.server.netty.EngineMain.main(args)
fun main(args: Array<String>): Unit {
    embeddedServer(Netty, port = 8000) {
        routing {
            get("/") {
                call.respondText("Hello, world!")
            }
        }
    }.start(wait = true)
}

@Suppress("unused") // Referenced in application.conf
@kotlin.jvm.JvmOverloads
fun Application.module(testing: Boolean = false) {
}


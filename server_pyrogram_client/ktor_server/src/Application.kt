package

import com.openproject.lib.loadConfig
import io.ktor.application.*
import io.ktor.response.*
import io.ktor.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import org.jetbrains.kotlin.konan.file.File


fun main(args: Array<String>): Unit {
    val config = loadConfig()
    embeddedServer(Netty, port = config.server.port) {
        routing {
            get(path = "/api/command/"){


            }
            get(path = "/api/"){
               call.respond(File("../src/server_settings/html/doc_api.html"))
            }
        }
    }.start(wait = true)
}




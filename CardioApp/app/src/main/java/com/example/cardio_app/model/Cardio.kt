import java.io.Serializable

data class Cardio (
    val frequencia: String = "",
    val timestamp: String = "",
) : Serializable {

    // Converte o objeto em um Map para enviar ao Firebase
    fun toMap(): Map<String, Any> {
        return mapOf( 
            "frequencia" to frequencia,
            "timestamp" to timestamp,
        )
    }

    // Cria um objeto a partir de um Map recebido do Firebase
    companion object {
        fun fromMap(map: Map<String, Map<String, Any>>) = Cardio(
            frequencia = map.values.first()["frequencia"] as? String ?: "",
            timestamp = map.values.first()["timestamp"] as? String ?: "",
        )
    }
}

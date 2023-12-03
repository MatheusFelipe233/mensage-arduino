package com.example.cardio_app

import Cardio
import android.os.Bundle
import android.util.Log
import android.widget.TextView
import androidx.activity.ComponentActivity
import com.google.firebase.database.DataSnapshot
import com.google.firebase.database.DatabaseError
import com.google.firebase.database.ValueEventListener
import com.google.firebase.database.ktx.database
import com.google.firebase.ktx.Firebase


class MainActivity : ComponentActivity() {

    private var lastHeartRate: String = "";
    private lateinit var cardioTextView : TextView;

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        cardioTextView = findViewById(R.id.text_view_cardio)


        // Write a message to the database
        val database = Firebase.database
        val refCardio = database.getReference("cardio")

        // para enviar dados ao firebase
//        val cardio = Cardio(frequencia = "9876", timestamp = "987")
//        myRef.setValue(cardio)

//        Log.i("Firebase","cardio send to firebase")

        refCardio.orderByKey().limitToLast(1).addValueEventListener(object : ValueEventListener {
            override fun onDataChange(dataSnapshot: DataSnapshot) {
                val cardioMap = dataSnapshot.value as Map<String, Map<String, Any>>
                val cardio = Cardio.fromMap(cardioMap)
                lastHeartRate = cardio.frequencia

                cardioTextView.text = lastHeartRate

                Log.i("Firebase", "Success reading realtime database. Heart rate: $lastHeartRate")
            }

            override fun onCancelled(error: DatabaseError) {
                // Failed to read value
                Log.w("Firebase", "Failed to read value.", error.toException())
            }
        })
    }
}
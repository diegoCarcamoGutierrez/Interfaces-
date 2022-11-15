package com.example.mycatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CatalogActivity extends AppCompatActivity {
    private Button catalog_button; //variable botón para la activity_catalog
    private Context context=this; //Contexto de la clase. No se puede usar this dentro de una función integrada en un protected void

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_catalog);
        catalog_button=findViewById(R.id.button); //conexion del boton
        catalog_button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent myIntent=new Intent(context,DetailActivity.class);
                context.startActivity(myIntent);
            }
        });
    }
}
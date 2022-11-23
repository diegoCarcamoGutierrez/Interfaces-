package com.example.myothercatalog;

import android.content.Context;
import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.RecyclerView;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonObjectRequest;
import com.android.volley.toolbox.Volley;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {
    private TextView description;
    private ImageView image;
    private Context context=this;
    private TextView name;
    private RecyclerView recyclerView;
    private RequestQueue listQueue;

    private void showImages(){
        JsonObjectRequest request= new JsonObjectRequest(
                Request.Method.GET,
                Server.name,
                null,
                new Response.Listener<JSONObject>() {
                    @Override
                    public void onResponse(JSONObject response) {
                        try {
                            JSONArray imageList = response.getJSONArray("data");

                        } catch (JSONException e) {
                            e.printStackTrace();
                        }
                    }
                },
                new Response.ErrorListener() {
                    @Override
                    public void onErrorResponse(VolleyError error) {
                        Toast.makeText(context,"An error has ocurred",Toast.LENGTH_SHORT).show();
                    }
                }
        );
        this.listQueue.add(request);
    }

}

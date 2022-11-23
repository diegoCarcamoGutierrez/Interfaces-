package com.example.myothercatalog;

import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class ImageViewHolder extends RecyclerView.ViewHolder {
    private TextView name;
    private ImageView image;
    private TextView desc;
    public ImageViewHolder(@NonNull View itemView) {
        super(itemView);
    }
}

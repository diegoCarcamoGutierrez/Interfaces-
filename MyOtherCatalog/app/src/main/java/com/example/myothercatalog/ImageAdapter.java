package com.example.myothercatalog;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class ImageAdapter extends RecyclerView.Adapter<ImageViewHolder> {

    private final TextView textView;
    private final ImageView imageView;

    public ImageAdapter(TextView textView, ImageView imageView){
        this.textView = textView;
        this.imageView = imageView;
    }

    @NonNull
    @Override
    public ImageViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        LayoutInflater inflater = LayoutInflater.from(parent.getContext());
        View cellView = inflater.inflate(R.layout.recycler_view_cell, parent, false);
        ImageViewHolder cellViewHolder=new ImageViewHolder(cellView);
        return cellViewHolder;
    }

    @Override
    public void onBindViewHolder(@NonNull ImageViewHolder holder, int position) {

    }


    @Override
    public int getItemCount() {
        return 0;
    }
}

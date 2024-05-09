from moviepy.editor import VideoFileClip
import os
import imageio

def extract_frames(video_path, output_path,num_frames):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Load the video file
    video = VideoFileClip(video_path)
    
    # Calculate the total number of frames and frame interval
    total_frames = int(video.fps * video.duration)
    frame_interval = max(total_frames // num_frames, 1)
    
    # Extract frames
    for i, frame in enumerate(video.iter_frames(fps=video.fps, dtype='uint8'), start=1):
        if i % frame_interval == 0:
            frame_filename = os.path.join(output_path, f"{i}.jpg")
            imageio.imwrite(frame_filename, frame)
            # print(f"Frame {i} saved as {frame_filename}")
        
        if i >= num_frames * frame_interval:
            break

    # Close the video file
    video.close()
    

if __name__ == "__main__":
    directory = '/home/rajesh/hostage_250/HOSTAGE_DATASET_KAGGLE/HOSTAGE'
    output_directory='/home/rajesh/hostage_250/HOSTAGE_DATASET_KAGGLE/HOSTAGE_FRAMES'
    num_frames = 50
    err_files = []
    i=0
    for videoname in os.listdir(directory):
        video_path=os.path.join(directory,videoname)
        output_video_folder=f"Hostage_{i}"
        output_path=os.path.join(output_directory,output_video_folder)
        try:
            extract_frames(video_path, output_path,num_frames)
        except Exception as e:
            err_files.append(videoname)
            print(f"Error processing file '{videoname}': {e}")
        i+=1
    print("Done successfully\n")
    print(err_files)

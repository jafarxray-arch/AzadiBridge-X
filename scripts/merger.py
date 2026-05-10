import os
import sys
import glob

def merge_files(prefix, output_name=None):
    parts = sorted(glob.glob(f"{prefix}*"))
    parts = [p for p in parts if 'checksums' not in p]
    
    if not parts:
        print(f"❌ No parts found with prefix: {prefix}")
        return False
    
    if not output_name:
        output_name = prefix.rstrip('_').rstrip('0123456789').rstrip('_')
        if not output_name or output_name == prefix:
            output_name = "merged_output"
    
    print(f"🔧 Merging {len(parts)} parts into: {output_name}")
    
    try:
        with open(output_name, 'wb') as out:
            for part in parts:
                with open(part, 'rb') as p:
                    out.write(p.read())
                print(f"  ✓ {part}")
        
        size = os.path.getsize(output_name)
        if size > 1024*1024:
            print(f"✅ Done! Size: {size/(1024*1024):.2f} MB")
        else:
            print(f"✅ Done! Size: {size/1024:.2f} KB")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python merger.py <part_prefix> [output_name]")
        print("Example: python merger.py video_part_ my_video.mp4")
        sys.exit(1)
    merge_files(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else None)

FILE="$1"
if [ -z "$FILE" ]; then
    echo "Usage: ./splitter.sh <filename>"
    exit 1
fi

DIR=$(dirname "$FILE")
BASENAME=$(basename "$FILE")
PREFIX="${BASENAME%.*}"

cd "$DIR" || exit 1

echo "🔪 Splitting: $BASENAME"
split -b 95M -d "$BASENAME" "${PREFIX}_part_"

# Generate checksums
md5sum "${PREFIX}_part_"* > "${PREFIX}_checksums.txt"

echo "✅ Split into: ${PREFIX}_part_00, ${PREFIX}_part_01, ..."
echo "📋 Checksums saved: ${PREFIX}_checksums.txt"
